# 🚀 Guía de Despliegue — Sabores Colombianos

Documentación del proceso de despliegue en **Google Cloud Platform**.

---

## ☁️ Arquitectura en GCP

```
Internet
    │
    ▼
Cloud Run (Frontend)          Cloud Run (Backend)
recetario-frontend            recetario-backend
HTML/CSS/JS + Nginx           FastAPI + Uvicorn
    │                              │
    └──────── HTTPS API ───────────┘
                                   │
                              Cloud SQL
                           PostgreSQL 15
                         recetario-495422:
                         us-central1:recetario-db
```

---

## 📋 Servicios configurados

| Servicio | Nombre | Región |
|---------|--------|--------|
| Cloud Run | recetario-frontend | us-central1 |
| Cloud Run | recetario-backend | us-central1 |
| Cloud SQL | recetario-db | us-central1 |
| Artifact Registry | recetario-repo | us-central1 |
| Secret Manager | DATABASE_URL | global |

---

## 🔧 Requisitos previos

```bash
# Instalar Google Cloud CLI
curl https://sdk.cloud.google.com | bash
gcloud init

# Autenticarse
gcloud auth login
gcloud config set project recetario-495422
```

---

## 🗄️ Configuración de base de datos

### Crear instancia Cloud SQL
```bash
gcloud sql instances create recetario-db \
  --database-version=POSTGRES_15 \
  --tier=db-f1-micro \
  --region=us-central1

# Crear base de datos
gcloud sql databases create recetario_db --instance=recetario-db

# Crear usuario
gcloud sql users set-password postgres \
  --instance=recetario-db \
  --password=MiPassword123!
```

### Configurar DATABASE_URL en Secret Manager
```bash
echo -n "postgresql://postgres:MiPassword123!@/recetario_db?host=/cloudsql/recetario-495422:us-central1:recetario-db" | \
  gcloud secrets create DATABASE_URL --data-file=-
```

---

## 🐳 Despliegue del Backend

```bash
cd /home/alexandrarivera510/Recetario

# 1. Build de la imagen
gcloud builds submit --config cloudbuild.yaml

# 2. Deploy en Cloud Run
gcloud run deploy recetario-backend \
  --image us-central1-docker.pkg.dev/recetario-495422/recetario-repo/backend:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-secrets=DATABASE_URL=DATABASE_URL:latest \
  --add-cloudsql-instances=recetario-495422:us-central1:recetario-db
```

---

## 🌐 Despliegue del Frontend

```bash
cd /home/alexandrarivera510/Recetario

# 1. Build y tag de la imagen
TAG="v$(date +%s)"
gcloud builds submit --tag gcr.io/recetario-495422/recetario-frontend:$TAG

# 2. Deploy en Cloud Run
gcloud run deploy recetario-frontend \
  --image gcr.io/recetario-495422/recetario-frontend:$TAG \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## 🔄 Migración de base de datos

Para agregar nuevas columnas sin bajar el servicio:

```bash
# Llamar al endpoint de migración (una sola vez)
curl https://recetario-backend-276307409989.us-central1.run.app/migrate
```

---

## ✅ Verificar despliegue

```bash
# Verificar backend
curl https://recetario-backend-276307409989.us-central1.run.app/

# Verificar recetas
curl https://recetario-backend-276307409989.us-central1.run.app/recetas/

# Ver logs
gcloud run logs read --service=recetario-backend --region=us-central1
```

---

## 🔍 Ver base de datos desde Cloud Shell

```bash
gcloud sql connect recetario-db --user=postgres --database=recetario_db
```

Queries útiles:
```sql
SELECT * FROM usuarios;
SELECT * FROM recetas;
SELECT COUNT(*) FROM favoritos;
SELECT COUNT(*) FROM comentarios;
```

---

## ⚠️ Problemas comunes

| Error | Causa | Solución |
|-------|-------|---------|
| Container failed to start | Error de sintaxis en Python | Revisar logs con `gcloud run logs read` |
| 500 en favoritos | Receta inexistente en DB | Verificar que la receta existe antes de guardar |
| CORS bloqueado | Origin no permitido | Verificar `allow_origins=["*"]` en main.py |
| DATABASE_URL no encontrada | Secret no configurado | `gcloud secrets versions access latest --secret="DATABASE_URL"` |

---

## 💰 Costos (Free Tier)

| Servicio | Free Tier |
|---------|-----------|
| Cloud Run | 2M requests/mes gratis |
| Cloud SQL (db-f1-micro) | ~$7/mes (no tiene free tier) |
| Artifact Registry | 0.5 GB gratis |
| Cloud Build | 120 min/día gratis |

> ⚠️ Apagar Cloud SQL cuando no se use para evitar costos.