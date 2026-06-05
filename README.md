# 🇨🇴 Sabores Colombianos

![GCP Cloud Run](https://img.shields.io/badge/deploy-Google%20Cloud%20Run-blue?logo=google-cloud)
![FastAPI](https://img.shields.io/badge/backend-FastAPI-green?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/database-PostgreSQL-blue?logo=postgresql)
![JavaScript](https://img.shields.io/badge/frontend-HTML%2FJS%2FCSS-yellow?logo=javascript)

Plataforma web full-stack para explorar, compartir y aprender recetas tradicionales colombianas. Desarrollada con FastAPI, PostgreSQL en Cloud SQL y desplegada en Google Cloud Platform.

---

## 👥 Equipo de Desarrollo

| Nombre | Rol |
|--------|-----|
| Alexandra Rivera | Product Owner · Backend Developer · Frontend Developer · DevOps Engineer |

---

## 🌐 URLs de acceso

| Servicio | URL |
|---------|-----|
| **Frontend** | https://recetario-frontend-276307409989.us-central1.run.app |
| **Backend API** | https://recetario-backend-276307409989.us-central1.run.app |
| **Documentación API** | https://recetario-backend-276307409989.us-central1.run.app/docs |
| **GitHub Project** | https://github.com/Alexandra510R/Recetario/projects |

---

## 🛠️ Stack tecnológico

| Capa | Tecnología |
|------|-----------|
| Backend | FastAPI (Python) |
| Base de datos | PostgreSQL — Cloud SQL |
| Frontend | HTML5 / CSS3 / JavaScript |
| Autenticación | JWT (python-jose) |
| ORM | SQLAlchemy |
| Hosting | Google Cloud Run |
| Contenedor | Docker |
| CI/CD | GitHub Actions + Google Cloud Build |

---

## ☁️ Servicios GCP utilizados

| Servicio | Uso |
|---------|-----|
| Cloud Run | Hosting del backend y frontend |
| Cloud SQL (PostgreSQL) | Base de datos relacional |
| Artifact Registry | Almacenamiento de imágenes Docker |
| Cloud Build | Build y deploy automatizado |
| Secret Manager | Variables de entorno seguras |

---

## 🏗️ Arquitectura del sistema

```
Usuario
   │
   ▼
Cloud Run (Frontend)
HTML / CSS / JS
   │
   ▼ HTTPS REST API
Cloud Run (Backend)
FastAPI + SQLAlchemy
   │
   ▼
Cloud SQL
PostgreSQL
```

---

## 📁 Estructura del repositorio

```
Recetario/
├── .github/
│   └── workflows/
│       ├── ci.yml                   ← CI: tests y build automático
│       └── project-automation.yml  ← Automatización del tablero Kanban
├── backend/
│   ├── main.py              ← Aplicación FastAPI principal
│   ├── models.py            ← Modelos SQLAlchemy
│   ├── schemas.py           ← Schemas Pydantic
│   ├── database.py          ← Conexión a PostgreSQL
│   ├── requirements.txt     ← Dependencias Python
│   └── routers/
│       ├── usuarios.py      ← Endpoints de usuarios
│       ├── recetas.py       ← Endpoints de recetas
│       ├── favoritos.py     ← Endpoints de favoritos
│       └── comentarios.py   ← Endpoints de comentarios
├── src/
│   ├── PaginaInicial.html
│   ├── Recetas.html
│   ├── Registro.html
│   ├── Perfil.html
│   ├── IaChef.html
│   ├── Calendario.html
│   ├── Admin.html
│   ├── SaberMas.html
│   ├── script.js
│   └── css/
│       └── style.css
├── Docs/
│   ├── README-api.md
│   └── README-deployment.md
├── Dockerfile               ← Frontend
├── Dockerfile.backend       ← Backend
├── cloudbuild.yaml          ← Build backend
├── cloudbuild-frontend.yaml ← Build frontend
└── default.conf             ← Configuración nginx
```

---

## 📋 Metodología de Gestión — Kanban

El proyecto se gestionó con **GitHub Projects** usando metodología Kanban con las siguientes columnas:

`Backlog → Ready → In Progress → In Review → Done`

### Campos personalizados configurados:
| Campo | Valores |
|-------|---------|
| Sprint | Sprint 1, Sprint 2, Sprint 3 |
| Prioridad | Alta, Media, Baja |
| Estimación | 1, 2, 3, 5, 8 (puntos de historia) |
| Tipo | Feature, Bug, Documentation, DevOps |

### Estrategia de ramas:
```
main
├── feature/sprint1-autenticacion-jwt
├── feature/sprint2-pagina-principal
├── feature/sprint3-despliegue-gcp
└── feature/sprint3-github-actions
```

---

## 🏃 Sprints Completados

### Sprint 1 — Backend & Base de datos
| Historia | Puntos | Estado |
|----------|--------|--------|
| HU-01: Registro de usuarios | 3 | ✅ Done |
| HU-02: Autenticación con JWT | 3 | ✅ Done |
| HU-03: CRUD de recetas | 5 | ✅ Done |
| HU-04: Categorías y filtros | 3 | ✅ Done |
| HU-05: Sistema de favoritos | 3 | ✅ Done |
| HU-06: Modelo de BD PostgreSQL | 2 | ✅ Done |

**Velocity Sprint 1: 19 puntos**

Evidencias: rama `feature/sprint1-autenticacion-jwt` → PR #30 mergeado a `main`.

---

### Sprint 2 — Frontend & UX
| Historia | Puntos | Estado |
|----------|--------|--------|
| HU-07: Página principal con recetas | 3 | ✅ Done |
| HU-08: Formulario de creación de receta | 3 | ✅ Done |
| HU-09: Buscador de recetas | 3 | ✅ Done |
| HU-10: Perfil de usuario | 2 | ✅ Done |
| HU-11: Vista detallada de receta | 2 | ✅ Done |
| HU-12: Diseño responsive | 3 | ✅ Done |

**Velocity Sprint 2: 16 puntos**

Evidencias: rama `feature/sprint2-pagina-principal` → PR mergeado a `main`.

---

### Sprint 3 — Despliegue & DevOps
| Historia | Puntos | Estado |
|----------|--------|--------|
| HU-13: Dockerización de la aplicación | 3 | ✅ Done |
| HU-14: Pipeline CI/CD con GitHub Actions | 5 | ✅ Done |
| HU-15: Despliegue en GCP | 5 | ✅ Done |
| HU-16: Gestión de secretos y variables | 2 | 👀 In Review |
| HU-17: Monitoreo y logs en GCP | 3 | 🔧 In Progress |
| HU-18: Documentación completa | 2 | 🔧 In Progress |

**Velocity Sprint 3: 15 puntos completados**

Evidencias: ramas `feature/sprint3-despliegue-gcp` y `feature/sprint3-github-actions` → PRs mergeados a `main`.

---

## 📊 Métricas del Proyecto

| Métrica | Valor |
|---------|-------|
| **Velocity promedio** | 17 puntos por sprint |
| **Total puntos completados** | 50 / 56 puntos |
| **Historias completadas** | 15 / 18 historias |
| **Historias en progreso** | 3 / 18 |
| **Bugs encontrados** | 5 |
| **Bugs resueltos** | 5 |
| **Pull Requests realizados** | 4 |
| **Ramas creadas** | 4 feature branches |
| **Sprints completados** | 3 / 3 |

---

## ⚙️ Instalación local

### Requisitos previos
- Python 3.11+
- PostgreSQL o acceso a Cloud SQL
- Git

### 1. Clonar el repositorio
```bash
git clone https://github.com/Alexandra510R/Recetario.git
cd Recetario
```

### 2. Configurar el backend
```bash
cd backend
pip install -r requirements.txt

# Configurar variable de entorno
export DATABASE_URL="postgresql://usuario:password@localhost/recetario_db"

# Ejecutar
uvicorn main:app --reload --port 8000
```

### 3. Ejecutar el frontend
```bash
cd src
python3 -m http.server 8080
# Abrir http://localhost:8080/PaginaInicial.html
```

---

## 🚀 Comandos de despliegue en GCP

```bash
# Backend
gcloud builds submit --config cloudbuild.yaml
gcloud run deploy recetario-backend \
  --image us-central1-docker.pkg.dev/recetario-495422/recetario-repo/backend:latest \
  --platform managed --region us-central1 --allow-unauthenticated

# Frontend
TAG="v$(date +%s)"
gcloud builds submit --tag gcr.io/recetario-495422/recetario-frontend:$TAG
gcloud run deploy recetario-frontend \
  --image gcr.io/recetario-495422/recetario-frontend:$TAG \
  --platform managed --region us-central1 --allow-unauthenticated
```

---

## 🔐 Credenciales de prueba

| Campo | Valor |
|-------|-------|
| Email | alexandrarivera510@gmail.com |
| Contraseña | (ver entrega privada) |

---

## ⚠️ Problemas encontrados y soluciones

| Problema | Solución |
|---------|---------|
| CORS bloqueando peticiones desde live-server | Configurar `allow_origins=["*"]` en FastAPI middleware |
| Favoritos con error 500 por recetas inexistentes | Agregar validación de existencia antes de guardar |
| Columna `usuario_id` no existía en tabla recetas | Crear endpoint `/migrate` para ALTER TABLE en caliente |
| Tokens JWT expirados sin manejo en frontend | Agregar try/catch y redirect a login |
| Script duplicado en Admin.html rompía funciones | Limpiar con python script de reemplazo de texto |

---

## 💡 Lecciones Aprendidas

- **Gestión de ramas:** Mantener una rama por funcionalidad facilita el control de cambios y evita conflictos en el código.
- **Historias de usuario:** Definir criterios de aceptación claros desde el inicio agiliza el desarrollo y la validación.
- **CI/CD:** Automatizar el build y despliegue con GitHub Actions reduce errores humanos y acelera las entregas.
- **Kanban:** Mantener el tablero actualizado diariamente permite identificar bloqueos a tiempo.
- **Docker:** Contenerizar la aplicación desde el inicio garantiza consistencia entre entornos de desarrollo y producción.
- **Variables de entorno:** Gestionar secretos con GCP Secret Manager es esencial para la seguridad en producción.

---

## 📚 Documentación

- [Backend](./backend/README.md)
- [API Endpoints](./Docs/README-api.md)
- [Guía de despliegue](./Docs/README-deployment.md)
- [Frontend](./src/README.md)