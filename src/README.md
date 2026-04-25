![AWS EC2](https://img.shields.io/badge/deploy-AWS%20EC2-orange?logo=amazon-aws)
![JavaScript CI](https://github.com/Alexandra510R/Recetario/workflows/JavaScript%20CI/badge.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)


# 💛💙❤️ **RECETARIO COLOMBIANO**

Documentación del frontend de la aplicación **Sabores Colombianos**, una plataforma web para explorar, compartir y aprender recetas tradicionales colombianas.

---

## 📁 Estructura de Archivos

```
src/
├── PaginaInicial.html     ← Página de inicio con hero, features y video
├── Recetas.html           ← Catálogo de recetas con favoritos y comentarios
├── Registro.html          ← Login y registro de usuarios
├── script.js              ← Lógica de conexión con la API
└── css/
    └── style.css          ← Estilos globales con temática colombiana
```

---

## 🖥️ Páginas

### 🏠 PaginaInicial.html
- Hero section con bienvenida y botones de acción
- Cards de características (recetas, videos, favoritos, comunidad)
- Video musical colombiano embebido
- Header dinámico según sesión activa

### 🍲 Recetas.html
- Catálogo de 3 recetas tradicionales (Ajiaco, Bandeja Paisa, Arepas)
- Botón de **favoritos** por receta (requiere sesión)
- Sección de **comentarios** por receta (requiere sesión)
- Sección de **recetas de la comunidad** cargadas desde la API
- Modal para **subir nuevas recetas** (requiere sesión)

### 📝 Registro.html
- **Tab de Login** — Inicia sesión con email y contraseña
- **Tab de Registro** — Formulario completo con:
  - Nombre, email, contraseña
  - Teléfono, edad, género
  - Área de interés y mensaje
- Sidebar con beneficios y últimos registros

---

## 🎨 Diseño

| Elemento | Valor |
|----------|-------|
| **Fuente principal** | Nunito |
| **Fuente de títulos** | Playfair Display |
| **Color primario** | `#003087` (Azul Colombia) |
| **Color secundario** | `#CE1126` (Rojo Colombia) |
| **Color acento** | `#F8D800` (Amarillo Colombia) |
| **Fondo** | `#FFFDF0` (Blanco cálido) |

---

## 🔗 Conexión con la API

El frontend se comunica con el backend FastAPI en:

```
http://127.0.0.1:8000  ← Local
http://3.18.225.21:8000 ← AWS EC2
```

Cambia la variable `API_URL` en `script.js` y en cada página HTML según el entorno.

---

## 💾 Sesión de Usuario

La sesión se maneja con `localStorage`:

```javascript
// Guardar sesión
localStorage.setItem('usuario', JSON.stringify(data));
localStorage.setItem('token', data.access_token);

// Leer sesión
const usuario = JSON.parse(localStorage.getItem('usuario'));

// Cerrar sesión
localStorage.removeItem('usuario');
localStorage.removeItem('token');
```

---

## 🚀 Cómo Ejecutar

**Opción 1 — Live Server (VS Code):**
1. Instala la extensión **Live Server**
2. Clic derecho en `PaginaInicial.html` → **Open with Live Server**
3. Se abre en `http://127.0.0.1:5500`

**Opción 2 — Servidor Python:**
```bash
python3 -m http.server 8080
```
Luego abre `http://127.0.0.1:8080/src/PaginaInicial.html`

> ⚠️ Asegúrate de tener el backend corriendo antes de probar funciones como login, favoritos o comentarios.

---

## 📌 Notas

- Los botones de favoritos y comentarios requieren **sesión activa**
- El modal de subir recetas aparece solo cuando el usuario está autenticado
- El header muestra el nombre del usuario cuando hay sesión activa
