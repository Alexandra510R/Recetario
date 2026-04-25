# ⚙️ Backend — Sabores Colombianos API

Documentación del backend de **Sabores Colombianos**, una API REST construida con FastAPI y PostgreSQL.

---

## 📁 Estructura de Archivos

```
backend/
├── main.py              ← Punto de entrada, configuración CORS y routers
├── database.py          ← Conexión a PostgreSQL con SQLAlchemy
├── models.py            ← Modelos de base de datos (tablas)
├── schemas.py           ← Esquemas de validación con Pydantic
├── requirements.txt     ← Dependencias del proyecto
└── routers/
    ├── __init__.py
    ├── usuarios.py      ← Registro y login de usuarios
    ├── recetas.py       ← CRUD de recetas
    ├── favoritos.py     ← Gestión de favoritos
    └── comentarios.py   ← Gestión de comentarios
```

---

## 🛠️ Tecnologías

| Librería | Versión | Uso |
|----------|---------|-----|
| **FastAPI** | latest | Framework principal de la API |
| **Uvicorn** | latest | Servidor ASGI |
| **SQLAlchemy** | 2.x | ORM para base de datos |
| **psycopg2-binary** | latest | Driver PostgreSQL |
| **python-dotenv** | latest | Variables de entorno |
| **passlib** | 1.7.4 | Encriptación de contraseñas |
| **bcrypt** | 4.0.1 | Algoritmo de hash |
| **python-jose** | latest | Tokens JWT |
| **pydantic[email]** | latest | Validación de emails |

---

## 🗄️ Base de Datos

### Tablas

**usuarios**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer PK | ID único |
| nombre | String(100) | Nombre completo |
| email | String(100) | Email único |
| password | String(255) | Contraseña encriptada |
| telefono | String(20) | Teléfono opcional |
| edad | Integer | Edad opcional |
| genero | String(20) | Género opcional |
| interes | String(100) | Área de interés |
| mensaje | Text | Mensaje opcional |
| created_at | DateTime | Fecha de registro |

**recetas**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer PK | ID único |
| titulo | String(200) | Nombre de la receta |
| region | String(100) | Región de Colombia |
| ingredientes | Text | Lista de ingredientes |
| pasos | Text | Pasos de preparación |
| video_url | String(500) | URL del video |
| imagen_url | String(500) | URL de la imagen |
| created_at | DateTime | Fecha de creación |

**favoritos**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer PK | ID único |
| usuario_id | Integer FK | Referencia a usuario |
| receta_id | Integer FK | Referencia a receta |

**comentarios**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer PK | ID único |
| contenido | Text | Texto del comentario |
| usuario_id | Integer FK | Referencia a usuario |
| receta_id | Integer FK | Referencia a receta |
| created_at | DateTime | Fecha del comentario |

---

## 🔌 Endpoints

### Usuarios `/usuarios`
| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/usuarios/registro` | Registrar nuevo usuario |
| POST | `/usuarios/login` | Iniciar sesión, retorna JWT |

### Recetas `/recetas`
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/recetas/` | Obtener todas las recetas |
| GET | `/recetas/{id}` | Obtener receta por ID |
| POST | `/recetas/` | Crear nueva receta |
| PUT | `/recetas/{id}` | Actualizar receta |
| DELETE | `/recetas/{id}` | Eliminar receta |

### Favoritos `/favoritos`
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/favoritos/{usuario_id}` | Ver favoritos de un usuario |
| POST | `/favoritos/` | Agregar a favoritos |
| DELETE | `/favoritos/{id}` | Eliminar de favoritos |

### Comentarios `/comentarios`
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/comentarios/{receta_id}` | Ver comentarios de una receta |
| POST | `/comentarios/` | Agregar comentario |
| DELETE | `/comentarios/{id}` | Eliminar comentario |

---

## ⚙️ Configuración

### Variables de entorno `.env`

```
DATABASE_URL=postgresql://postgres:TU_PASSWORD@localhost:5432/recetario_db
SECRET_KEY=clave_secreta_recetario
```

### Instalar dependencias

```bash
# Crear entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

# Instalar
pip install -r backend/requirements.txt
pip install bcrypt==4.0.1 passlib==1.7.4 pydantic[email]
```

---

## 🚀 Cómo Ejecutar

```bash
# Activar entorno virtual
venv\Scripts\activate

# Correr el servidor
uvicorn backend.main:app --reload
```

La API estará disponible en:
- **API:** `http://127.0.0.1:8000`
- **Documentación Swagger:** `http://127.0.0.1:8000/docs`
- **Documentación ReDoc:** `http://127.0.0.1:8000/redoc`

---

## 🔐 Seguridad

- Las contraseñas se encriptan con **bcrypt** antes de guardarse
- El login retorna un **token JWT** con expiración de 24 horas
- CORS configurado para aceptar peticiones desde `http://127.0.0.1:5500`

---

## 📌 Notas importantes

- Usar **bcrypt==4.0.1** y **passlib==1.7.4** para evitar errores de compatibilidad
- Si se modifican los modelos, eliminar y recrear las tablas en pgAdmin:
```sql
DROP TABLE IF EXISTS comentarios, favoritos, usuarios, recetas CASCADE;
```
Las tablas se recrean automáticamente al reiniciar uvicorn.
