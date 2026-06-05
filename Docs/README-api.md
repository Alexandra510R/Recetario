# 📡 Documentación de API — Sabores Colombianos

Base URL: `https://recetario-backend-276307409989.us-central1.run.app`

Documentación interactiva: `/docs` (Swagger UI)

---

## 👤 Usuarios

### POST /usuarios/registro
Crear una nueva cuenta de usuario.

**Request:**
```json
{
  "nombre": "María García",
  "email": "maria@email.com",
  "password": "miPassword123",
  "telefono": "3001234567",
  "edad": 25,
  "genero": "femenino",
  "interes": "recetas",
  "mensaje": "Me encanta la cocina colombiana"
}
```

**Response 200:**
```json
{
  "id": 1,
  "nombre": "María García",
  "email": "maria@email.com",
  "telefono": "3001234567",
  "edad": 25,
  "genero": "femenino",
  "interes": "recetas",
  "mensaje": "Me encanta la cocina colombiana",
  "created_at": "2026-06-05T10:00:00"
}
```

**Response 400:**
```json
{ "detail": "El email ya está registrado" }
```

---

### POST /usuarios/login
Iniciar sesión y obtener token JWT.

**Request:**
```json
{
  "nombre": "login",
  "email": "maria@email.com",
  "password": "miPassword123"
}
```

**Response 200:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer",
  "usuario": {
    "id": 1,
    "nombre": "María García",
    "email": "maria@email.com",
    "telefono": "3001234567",
    "edad": 25,
    "genero": "femenino",
    "interes": "recetas",
    "mensaje": "Me encanta la cocina colombiana"
  }
}
```

**Response 401:**
```json
{ "detail": "Credenciales incorrectas" }
```

---

### GET /usuarios/
Listar todos los usuarios.

**Response 200:**
```json
[
  { "id": 1, "nombre": "María García", "email": "maria@email.com", ... },
  { "id": 2, "nombre": "Juan López", "email": "juan@email.com", ... }
]
```

---

### GET /usuarios/{usuario_id}
Obtener un usuario por ID.

**Response 200:**
```json
{ "id": 1, "nombre": "María García", "email": "maria@email.com", ... }
```

**Response 404:**
```json
{ "detail": "Usuario no encontrado" }
```

---

### PUT /usuarios/{usuario_id}
Actualizar información del perfil.

**Request:**
```json
{
  "nombre": "María García",
  "telefono": "3009876543",
  "edad": 26,
  "genero": "femenino",
  "interes": "eventos",
  "mensaje": "Nueva bio"
}
```

**Response 200:**
```json
{
  "mensaje": "Perfil actualizado correctamente",
  "usuario": { "id": 1, "nombre": "María García", ... }
}
```

---

### PUT /usuarios/{usuario_id}/password
Cambiar contraseña.

**Request:**
```json
{
  "password_actual": "miPassword123",
  "password_nueva": "nuevaPassword456"
}
```

**Response 200:**
```json
{ "mensaje": "Contraseña actualizada correctamente" }
```

**Response 400:**
```json
{ "detail": "La contraseña actual es incorrecta" }
```

---

### DELETE /usuarios/{usuario_id}
Eliminar cuenta de usuario.

**Response 200:**
```json
{ "mensaje": "Usuario eliminado correctamente" }
```

---

## 🍲 Recetas

### GET /recetas/
Listar todas las recetas. Soporta filtro por usuario.

**Query params:**
- `usuario_id` (opcional) — filtrar recetas de un usuario específico

**Ejemplos:**
```
GET /recetas/
GET /recetas/?usuario_id=1
```

**Response 200:**
```json
[
  {
    "id": 14,
    "titulo": "Ajiaco Santafereño",
    "region": "Bogotá",
    "ingredientes": "Pechuga de pollo, Papa criolla, Guascas",
    "pasos": "1. Hervir el pollo...",
    "video_url": "https://youtu.be/otLZDxQH28A",
    "imagen_url": "",
    "usuario_id": null,
    "created_at": "2026-06-05T10:00:00"
  }
]
```

---

### GET /recetas/{receta_id}
Obtener una receta por ID.

**Response 404:**
```json
{ "detail": "Receta no encontrada" }
```

---

### POST /recetas/
Crear una nueva receta.

**Query params:**
- `usuario_id` (opcional) — asociar receta a un usuario

**Request:**
```json
{
  "titulo": "Sancocho de Gallina",
  "region": "Antioquia",
  "ingredientes": "Gallina, Papa, Yuca, Plátano, Cilantro",
  "pasos": "1. Hervir la gallina con cebolla...",
  "video_url": "https://youtu.be/...",
  "imagen_url": ""
}
```

**Response 200:**
```json
{
  "id": 15,
  "titulo": "Sancocho de Gallina",
  "region": "Antioquia",
  "usuario_id": 1,
  "created_at": "2026-06-05T10:30:00"
}
```

---

### PUT /recetas/{receta_id}
Actualizar una receta existente.

**Response 404:**
```json
{ "detail": "Receta no encontrada" }
```

---

### DELETE /recetas/{receta_id}
Eliminar una receta.

**Response 200:**
```json
{ "mensaje": "Receta eliminada correctamente" }
```

---

## ❤️ Favoritos

### GET /favoritos/{usuario_id}
Obtener favoritos de un usuario (solo recetas que existen).

**Response 200:**
```json
[
  { "id": 1, "usuario_id": 1, "receta_id": 14 },
  { "id": 2, "usuario_id": 1, "receta_id": 15 }
]
```

---

### POST /favoritos/
Toggle de favorito — agrega si no existe, elimina si ya existe.

**Query params:**
- `usuario_id` (requerido)

**Request:**
```json
{ "receta_id": 14 }
```

**Response — añadido:**
```json
{ "mensaje": "Añadido a favoritos", "action": "added", "id": 1 }
```

**Response — eliminado:**
```json
{ "mensaje": "Eliminado de favoritos", "action": "removed" }
```

**Response 404:**
```json
{ "detail": "Receta no encontrada" }
```

---

### DELETE /favoritos/{favorito_id}
Eliminar un favorito por ID.

**Response 200:**
```json
{ "mensaje": "Favorito eliminado correctamente" }
```

---

## 💬 Comentarios

### GET /comentarios/{receta_id}
Obtener comentarios de una receta.

**Response 200:**
```json
[
  {
    "id": 10,
    "contenido": "Excelente receta, la preparé ayer",
    "usuario_id": 1,
    "receta_id": 14,
    "created_at": "2026-06-05T12:00:00"
  }
]
```

---

### POST /comentarios/
Agregar un comentario a una receta.

**Query params:**
- `usuario_id` (requerido)

**Request:**
```json
{
  "contenido": "Esta receta es deliciosa",
  "receta_id": 14
}
```

**Response 200:**
```json
{
  "id": 11,
  "contenido": "Esta receta es deliciosa",
  "usuario_id": 1,
  "receta_id": 14,
  "created_at": "2026-06-05T12:30:00"
}
```

---

### DELETE /comentarios/{comentario_id}
Eliminar un comentario.

**Response 200:**
```json
{ "mensaje": "Comentario eliminado correctamente" }
```

---

## 📊 Códigos de estado HTTP

| Código | Significado |
|--------|-------------|
| 200 | Operación exitosa |
| 400 | Error en la solicitud (ej: email duplicado) |
| 401 | No autorizado (credenciales incorrectas) |
| 404 | Recurso no encontrado |
| 500 | Error interno del servidor |

---

## 🔗 Relación entre entidades

```
GET /favoritos/{usuario_id}     → Favoritos de un usuario (usuario → recetas)
GET /recetas/?usuario_id={id}   → Recetas de un usuario
GET /comentarios/{receta_id}    → Comentarios de una receta
```