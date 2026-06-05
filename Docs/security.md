# 🔐 Análisis de Seguridad — Sabores Colombianos

## Vulnerabilidades Identificadas y Medidas Implementadas

### 1. Endpoints sin autenticación
**Descripción:** Los endpoints de creación, actualización y eliminación de recetas estaban públicos, permitiendo que cualquier usuario sin autenticar pudiera modificar o eliminar datos.

**Medida implementada:** Se agregó autenticación JWT obligatoria en todos los endpoints POST, PUT y DELETE del router de recetas. Los endpoints GET permanecen públicos para permitir la consulta libre de recetas.

**Estado:** ✅ Resuelto

---

### 2. Credenciales expuestas en el código
**Descripción:** La `SECRET_KEY` usada para firmar tokens JWT tenía un valor por defecto hardcodeado en el código fuente (`clave_secreta_recetario`), lo que representa un riesgo si el repositorio es público.

**Medida implementada:** La clave se lee desde variables de entorno con `os.getenv("SECRET_KEY", ...)`. En producción se gestiona mediante GCP Secret Manager.

**Medida pendiente:** Eliminar el valor por defecto del código y forzar que la variable de entorno sea obligatoria. No se implementó aún para facilitar el desarrollo local sin configuración adicional.

**Estado:** ⚠️ Parcialmente resuelto

---

### 3. CORS abierto para todos los orígenes
**Descripción:** La configuración `allow_origins=["*"]` en el middleware de FastAPI permite que cualquier dominio haga peticiones a la API, lo que puede facilitar ataques CSRF.

**Medida implementada:** Se documentó el riesgo. La configuración actual es necesaria para permitir el acceso desde el frontend desplegado en Cloud Run con dominio dinámico.

**Medida pendiente:** Restringir los orígenes permitidos a los dominios específicos del frontend en producción una vez estabilizadas las URLs de Cloud Run.

**Estado:** ⚠️ Pendiente

---

### 4. Falta de rate limiting
**Descripción:** La API no tiene límite de peticiones por IP o por usuario, lo que la hace vulnerable a ataques de fuerza bruta en el endpoint `/login` y a ataques de denegación de servicio (DoS).

**Medida implementada:** No se implementó aún.

**Medida pendiente:** Integrar `slowapi` (rate limiter para FastAPI) para limitar intentos de login y peticiones por IP. No se implementó por restricciones de tiempo del proyecto.

**Estado:** ❌ Pendiente

---

### 5. Contraseñas sin longitud mínima
**Descripción:** El endpoint de registro no valida longitud mínima ni complejidad de contraseñas, permitiendo contraseñas débiles como "1234".

**Medida implementada:** Las contraseñas se almacenan hasheadas con bcrypt, lo que protege los datos en caso de filtración de la base de datos.

**Medida pendiente:** Agregar validación de longitud mínima (8 caracteres) y complejidad en el schema de Pydantic.

**Estado:** ⚠️ Parcialmente resuelto

---

## Plan de Respuesta a Incidentes

Si el equipo detecta acceso no autorizado o datos comprometidos, se seguirán estos pasos:

1. **Contención inmediata:** Revocar todos los tokens JWT activos rotando la `SECRET_KEY` en GCP Secret Manager y redesplegar el backend. Esto invalida todas las sesiones activas.
2. **Evaluación del daño:** Revisar los logs en GCP Cloud Logging para identificar qué endpoints fueron accedidos, desde qué IPs y en qué rango de tiempo.
3. **Notificación:** Informar a los usuarios afectados por email indicando que deben cambiar su contraseña.
4. **Corrección:** Identificar y parchear la vulnerabilidad explotada antes de volver a poner el servicio en línea.
5. **Post-mortem:** Documentar el incidente, causa raíz y medidas implementadas para evitar recurrencia.