# ⚙️ Backend — Sabores Colombianos

Documentación del backend de la aplicación **Sabores Colombianos**, construido con **FastAPI** y **PostgreSQL**.

---

## 🛠️ Stack

| Tecnología | Versión | Uso |
|-----------|---------|-----|
| Python | 3.11 | Lenguaje principal |
| FastAPI | 0.104+ | Framework REST API |
| SQLAlchemy | 2.0+ | ORM |
| Pydantic | 2.0+ | Validación de datos |
| python-jose | 3.3+ | JWT tokens |
| passlib/bcrypt | 1.7+ | Hash de contraseñas |
| httpx | 0.25+ | Cliente HTTP async |
| PostgreSQL | 15 | Base de datos |

---

## 📁 Estructura

```
backend/
├── main.py              ← App principal, CORS, routers, endpoint /migrate
├── database.py          ← Conexión SQLAlchemy a PostgreSQL
├── models.py            ← Tablas: Usuario, Receta, Favorito, Comentario
├── schemas.py           ← Schemas Pydantic para request/response
├── requirements.txt
└── routers/
    ├── usuarios.py      ← Registro, login, CRUD usuarios
    ├── recetas.py       ← CRUD recetas con filtro por usuario
    ├── favoritos.py     ← Toggle favoritos por usuario
    └── comentarios.py   ← Comentarios por receta
```

---

## 🗄️ Modelo de datos

### Entidad 1 — Usuario
```
usuarios
├── id           INTEGER PK
├── nombre       VARCHAR(100)
├── email        VARCHAR(100) UNIQUE
├── password     VARCHAR(255)  ← bcrypt hash
├── telefono     VARCHAR(20)
├── edad         INTEGER
├── genero       VARCHAR(20)
├── interes      VARCHAR(100)
├── mensaje      TEXT
└── created_at   TIMESTAMP
```

### Entidad 2 — Receta
```
recetas
├── id           INTEGER PK
├── titulo       VARCHAR(200)
├── region       VARCHAR(100)
├── ingredientes TEXT
├── pasos        TEXT
├── video_url    VARCHAR(500)
├── imagen_url   VARCHAR(500)
├── usuario_id   INTEGER FK → usuarios.id  (nullable)
└── created_at   TIMESTAMP
```

### Entidad 3 — Favorito (relación entre Usuario y Receta)
```
favoritos
├── id           INTEGER PK
├── usuario_id   INTEGER FK → usuarios.id
└── receta_id    INTEGER FK → recetas.id
```

### Entidad 4 — Comentario
```
comentarios
├── id           INTEGER PK
├── contenido    TEXT
├── usuario_id   INTEGER FK → usuarios.id
├── receta_id    INTEGER FK → recetas.id
└── created_at   TIMESTAMP
```

---

## 🔧 Configuración local

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Variable de entorno
export DATABASE_URL="postgresql://postgres:password@localhost/recetario_db"

# 3. Ejecutar
uvicorn backend.main:app --reload --port 8000
```

---

## 🐳 Docker

```bash
# Construir imagen
docker build -f Dockerfile.backend -t recetario-backend .

# Ejecutar
docker run -p 8000:8000 \
  -e DATABASE_URL="postgresql://..." \
  recetario-backend
```

---

## 🔐 Autenticación

El sistema usa **JWT tokens** con expiración de 24 horas.

```
POST /usuarios/login
→ Devuelve: { access_token, token_type, usuario: { id, nombre, email, ... } }
```

El token se guarda en `localStorage` en el frontend y se usa para identificar al usuario en operaciones de favoritos, comentarios y recetas.

---

## 🌐 URL en producción

```
https://recetario-backend-276307409989.us-central1.run.app
https://recetario-backend-276307409989.us-central1.run.app/docs
```