# 🎨 Frontend — Sabores Colombianos

Documentación del frontend de la aplicación **Sabores Colombianos**, desarrollado con HTML5, CSS3 y JavaScript vanilla.

---

## 📁 Estructura de archivos

```
src/
├── PaginaInicial.html     ← Página de inicio con hero section
├── Recetas.html           ← Catálogo de recetas con favoritos y comentarios
├── Registro.html          ← Login y registro de usuarios
├── Perfil.html            ← Perfil de usuario con edición de datos
├── IaChef.html            ← Generador de recetas con IA
├── Calendario.html        ← Planificador semanal de comidas
├── Admin.html             ← Panel de administración
├── SaberMas.html          ← Información sobre gastronomía colombiana
├── script.js              ← Lógica global: auth, nav, toast, API_URL
└── css/
    └── style.css          ← Sistema de diseño completo con variables CSS
```

---

## 🖥️ Páginas

### 🏠 PaginaInicial.html
- Hero section con gradiente azul Colombia
- Botones de acción (Ver recetas / Saber más)
- Footer con pie de página

### 🍲 Recetas.html
- Hero con estadísticas del recetario
- Buscador con filtros por región
- 3 recetas clásicas estáticas con imágenes
- Favoritos con toggle real en backend
- Comentarios guardados en base de datos
- Sección de recetas de la comunidad (API)
- Modal para subir nuevas recetas

### 📝 Registro.html
- Diseño de pantalla dividida (panel azul + formulario)
- Tab de Login con JWT
- Tab de Registro con datos completos
- Beneficios de la plataforma

### 👤 Perfil.html
- Foto de perfil con persistencia en localStorage
- Edición de información personal (PUT /usuarios/{id})
- Cambio de contraseña seguro (PUT /usuarios/{id}/password)
- Mis recetas filtradas por usuario
- Mis favoritos cargados desde backend
- Zona de peligro (eliminar recetas / eliminar cuenta)

### 🤖 IaChef.html
- Ingreso de ingredientes disponibles
- Búsqueda en recetas de la comunidad
- Base local de 10 recetas colombianas con puntuación
- Sugerencia de la receta con mayor coincidencia

### 📅 Calendario.html
- Calendario mensual navegable
- Plan semanal con 7 días
- Generador aleatorio de menú
- Edición de cada día

### ⚙️ Admin.html
- Dashboard con estadísticas en tiempo real
- Gestión de recetas (ver y eliminar)
- Gestión de usuarios (ver y eliminar)
- Moderación de comentarios
- Estadísticas por región

---

## 🎨 Sistema de diseño

| Variable | Valor | Uso |
|----------|-------|-----|
| `--azul` | `#003087` | Color Colombia, nav, hero |
| `--amarillo` | `#F5A623` | Acento, botones principales |
| `--rojo` | `#C0392B` | Alertas, danger |
| `--bg` | `#F7F5F0` / `#1A1F2E` | Fondo claro / oscuro |
| `--bg-card` | `#FFFFFF` / `#232A3E` | Cards |
| `--text` | `#1A1A1A` / `#EDF0F7` | Texto principal |

**Fuentes:**
- Títulos: `Playfair Display` (serif, elegante)
- Cuerpo: `DM Sans` (sans-serif, limpio)

**Modo oscuro:** Paleta azul marino automática con `[data-theme="dark"]`

---

## 🔗 Conexión con la API

La URL del backend se define en `script.js`:

```javascript
const API_URL = 'https://recetario-backend-276307409989.us-central1.run.app';
```

---

## 💾 Manejo de sesión

```javascript
// Guardar al hacer login
localStorage.setItem('token', data.access_token);
localStorage.setItem('usuario', JSON.stringify(data.usuario));

// Leer sesión
const usuario = JSON.parse(localStorage.getItem('usuario'));

// Cerrar sesión
localStorage.removeItem('token');
localStorage.removeItem('usuario');
```

Los datos de perfil persisten en `perfil_datos` — clave permanente que sobrevive al logout y se fusiona al iniciar sesión.

---

## 🚀 Cómo ejecutar localmente

```bash
# Opción 1 — Live Server (VS Code)
# Instalar extensión Live Server
# Clic derecho en PaginaInicial.html → Open with Live Server

# Opción 2 — Python
cd src
python3 -m http.server 8080
# Abrir http://localhost:8080/PaginaInicial.html
```

---

## 🌐 URL en producción

```
https://recetario-frontend-276307409989.us-central1.run.app
```

---

## 📱 Responsive

El frontend es responsive con breakpoint en `768px`:
- En móvil: nav colapsado en menú hamburguesa
- Hero adaptado a una sola columna
- Grid de recetas de 3 columnas → 1 columna