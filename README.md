![AWS EC2](https://img.shields.io/badge/deploy-AWS%20EC2-orange?logo=amazon-aws)
![JavaScript CI](https://github.com/Alexandra510R/Recetario/workflows/JavaScript%20CI/badge.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)


# 💛💙❤️ **RECETARIO COLOMBIANO**
Plataforma web diseñada para que los amantes de la cocina puedan explorar, aprender y compartir recetas auténticas de todas las regiones de Colombia.

---

## 🌐 Demo

| Servicio | URL |
|---------|-----|
| **Frontend local** | `http://127.0.0.1:5500/src/PaginaInicial.html` |
| **API local** | `http://127.0.0.1:8000` |
| **Documentación API** | `http://127.0.0.1:8000/docs` |
| **Servidor AWS** | `http://3.18.225.21:8000` |

---

## ✨ Funcionalidades

- 🍲 Catálogo de recetas tradicionales colombianas con ingredientes y videos
- ❤️ Sistema de favoritos por usuario
- 💬 Comentarios en recetas
- 🍳 Subir recetas propias
- 🔐 Registro e inicio de sesión con JWT
- ☁️ Despliegue en AWS EC2

---

## 📁 Estructura del Proyecto

```
Recetario/
├── src/                        ← Frontend
│   ├── PaginaInicial.html      ← Página de inicio
│   ├── Recetas.html            ← Catálogo de recetas
│   ├── Registro.html           ← Login y registro
│   ├── script.js               ← Lógica de conexión API
│   └── css/
│       └── style.css           ← Estilos globales
├── backend/                    ← API REST
│   ├── main.py                 ← Punto de entrada
│   ├── database.py             ← Conexión PostgreSQL
│   ├── models.py               ← Modelos de base de datos
│   ├── schemas.py              ← Validación de datos
│   ├── requirements.txt        ← Dependencias Python
│   └── routers/
│       ├── usuarios.py         ← Registro y login
│       ├── recetas.py          ← CRUD recetas
│       ├── favoritos.py        ← Gestión favoritos
│       └── comentarios.py      ← Gestión comentarios
├── .github/
│   ├── workflows/
│   │   └── JavaScriptCI.yml    ← CI con GitHub Actions
│   └── despliegue-aws.md       ← Documentación AWS
├── test/
│   └── basic.test.js           ← Tests con Jest
├── .env                        ← Variables de entorno (no subir)
├── .gitignore
├── Dockerfile
└── default.conf                ← Configuración Nginx
```

---

## 🛠️ Tecnologías

### Frontend
| Tecnología | Uso |
|-----------|-----|
| HTML5 / CSS3 | Estructura y estilos |
| JavaScript (Vanilla) | Lógica del cliente |
| Google Fonts | Playfair Display + Nunito |
| Live Server | Servidor de desarrollo |

### Backend
| Tecnología | Uso |
|-----------|-----|
| FastAPI | Framework de la API |
| Uvicorn | Servidor ASGI |
| SQLAlchemy | ORM |
| PostgreSQL | Base de datos |
| passlib + bcrypt | Encriptación de contraseñas |
| python-jose | Tokens JWT |

### Infraestructura
| Tecnología | Uso |
|-----------|-----|
| AWS EC2 | Servidor en la nube |
| Ubuntu 24.04 LTS | Sistema operativo del servidor |
| Docker + Nginx | Contenedor y servidor web |
| GitHub Actions | CI/CD |

---

## ⚙️ Instalación y Configuración

### Requisitos previos
- Python 3.x
- PostgreSQL 18
- Node.js (para tests)
- VS Code + extensión Live Server
- Git

### 1 — Clonar el repositorio
```bash
git clone https://github.com/Alexandra510R/Recetario.git
cd Recetario
```

### 2 — Crear el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac
```

### 3 — Instalar dependencias
```bash
pip install -r backend/requirements.txt
pip install bcrypt==4.0.1 passlib==1.7.4 pydantic[email]
```

### 4 — Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto:
```
DATABASE_URL=postgresql://postgres:TU_PASSWORD@localhost:5432/recetario_db
SECRET_KEY=clave_secreta_recetario
```

### 5 — Crear la base de datos
En pgAdmin4 o psql ejecuta:
```sql
CREATE DATABASE recetario_db;
```

---

## 🚀 Cómo Ejecutar

### Backend
```bash
# Activar entorno virtual
venv\Scripts\activate

# Correr el servidor
uvicorn backend.main:app --reload
```
✅ API disponible en `http://127.0.0.1:8000`

### Frontend
1. Abre `src/PaginaInicial.html` en VS Code
2. Clic derecho → **Open with Live Server**

✅ Frontend disponible en `http://127.0.0.1:5500/src/PaginaInicial.html`

---

## 🔌 Endpoints de la API

### Usuarios
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/usuarios/registro` | Registrar usuario |
| POST | `/usuarios/login` | Iniciar sesión |

### Recetas
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/recetas/` | Listar recetas |
| GET | `/recetas/{id}` | Ver receta |
| POST | `/recetas/` | Crear receta |
| PUT | `/recetas/{id}` | Editar receta |
| DELETE | `/recetas/{id}` | Eliminar receta |

### Favoritos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/favoritos/{usuario_id}` | Ver favoritos |
| POST | `/favoritos/` | Agregar favorito |
| DELETE | `/favoritos/{id}` | Eliminar favorito |

### Comentarios
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/comentarios/{receta_id}` | Ver comentarios |
| POST | `/comentarios/` | Agregar comentario |
| DELETE | `/comentarios/{id}` | Eliminar comentario |

---

## 🧪 Tests

```bash
npm test
```

Los tests están en `test/basic.test.js` y usan **Jest** con **jsdom**.

---

## ☁️ Despliegue en AWS EC2

| Parámetro | Valor |
|-----------|-------|
| **Instancia** | t3.micro |
| **SO** | Ubuntu Server 24.04 LTS |
| **IP Pública** | 3.18.225.21 |
| **Puertos abiertos** | 22, 80, 443, 8000 |

Para más detalles ver [`.github/README.md`](.github/README.md)

---

## ⚠️ Solución de Problemas

| Error | Solución |
|-------|---------|
| `connection refused port 5432` | Inicia el servicio PostgreSQL |
| `password cannot be longer than 72 bytes` | `pip install bcrypt==4.0.1 passlib==1.7.4` |
| `ModuleNotFoundError` | `pip install -r backend/requirements.txt` |
| Error CORS | Verifica que uvicorn esté corriendo en puerto 8000 |
| Tablas no existen | Ejecuta `DROP TABLE IF EXISTS comentarios, favoritos, usuarios, recetas CASCADE;` en pgAdmin y reinicia uvicorn |

---

## 🤝 Contribuir

1. Crea un issue describiendo el cambio
2. Crea una rama: `git checkout -b feature/nombre-del-cambio`
3. Realiza los cambios y haz commit: `git commit -m "feat: descripción #numero-issue"`
4. Sube la rama: `git push origin feature/nombre-del-cambio`
5. Crea un Pull Request con `Closes #numero-issue` en la descripción

---

## 📄 Licencia

&copy; 2025 Sabores Colombianos — Hecho con ❤️ desde Colombia 🇨🇴
