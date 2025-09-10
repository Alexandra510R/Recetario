![AWS EC2](https://img.shields.io/badge/deploy-AWS%20EC2-orange?logo=amazon-aws)
![JavaScript CI](https://github.com/Alexandra510R/Recetario/workflows/JavaScript%20CI/badge.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)


# 💛💙❤️ **RECETARIO COLOMBIANO**

Esta plataforma web esta diseñada par que los amantes de la cocina pueden explorar, aprender y compartir recetas auténticas de todas las regiones del país de Colombia

## 🔎 ¿Qué se puede hacer en la app?

__Descubrir recetas tradicionales:__ Se podran encuentrar platos típicos de cada rincón de Colombia, con ingredientes y pasos detallados.

__Aprender a cocinar:__ Tutoriales fáciles de seguir, desde el sancocho hasta los buñuelos.

__Unirte a la comunidad:__ Regístrate para guardar tus recetas favoritas, comentar y compartir tus propias creaciones culinarias.

## ✍️ Como funciona

La aplicación está organizada en tres secciones principales, cada una accesible desde el menú: Inicio, Recetario y Formulario.

Inicio: Presenta una breve descripción de la propuesta de la aplicación, acompañada de un video musical colombiano que resalta la riqueza cultural y las bellezas de nuestra región.

Recetario: Ofrece tres recetas tradicionales colombianas, con el listado detallado de ingredientes y un video explicativo que guía paso a paso en la preparación de cada plato.

Formulario: Contiene un espacio de registro que permite a los usuarios inscribirse para seguir recibiendo nuevos recetarios o, si lo desean, compartir sus propios conocimientos gastronómicos.

# 📋 Requisitos Previos

- Instancia EC2 creada y corriendo
- Security Group configurado con puertos 22 (SSH) y 8000 (desarrollo)
- Acceso SSH a la instancia
- Descarga de repositorio GitHub

# 🧱 Pasos de implementación

Antes de la implementación, es necesario contar con una instancia configurada y con la aplicación web que se desea desplegar para llevar a cabo el proceso.

## ▶️ Paso 1: Conectarse a la Instancia EC2

1. Ve a AWS Console → EC2 → Instances
2. Selecciona tu instancia
3. Clic en "Connect"
4. Selecciona "EC2 Instance Connect"
5. Clic en "Connect"

## 🔧 Paso 2: Preparar el Entorno

Actualizar sistema e instalar dependencias:

```
sudo apt update
sudo apt upgrade -y
sudo apt install python3-pip python3-venv
```

## ⏬ Paso 3: Clonar el Repositorio

- Ingresar a [GitHub](https://github.com/?utm_source=chatgpt.com)
- Crear un nuevo repositorio en tu cuenta.
- Seleccionar la opción <> Code y copiar la URL del repositorio.
- Abrir la terminal y ejecutar el siguiente comando para clonar el repositorio:

```
git clone https://github.com/Alexandra510R/Recetario.git
```

- Crear un nuevo repositorio en tu cuenta.

Seleccionar la opción <> Code y copiar la URL del repositorio.

Abrir la terminal y ejecutar el siguiente comando para clonar el repositorio:
``cd Recetario``

## 💻 Paso 4: CREAR ESTRUCTURA DE APLICACIÓN

- HTML/CSS/JS desde Visual Studio Code
- Asegurar que los archivos esten creados en la carpeta del respositorio

## 🔁 Paso 5: Actualizaciones

- Para enviar los cambios realizados desde tu equipo local al repositorio en GitHub, sigue estos pasos en la terminal:

```
git add . # Añade todos los cambios realizados
git commit -m "Mensaje descriptivo"   # Registra los cambios con un comentario
git push origin main   # Envía los cambios al repositorio remoto en la rama principal

```

- Finalmente, confirma en la página del repositorio [GitHub](https://github.com/Alexandra510R/Recetario.git)

## 📰 Paso 6: Configurar Entorno Virtual

- ### Crear entorno virtual

  ```python3 -m venv .venv```
- ### Activar entorno virtual

  ```source .venv/bin/**activate```
  📦 Paso 5: Instalar Dependencias
  ```pip install -r requirements.txt```

## 📂 Paso 7: Configurar Base de Datos

- ### Crear archivos de migración

  ```python manage.py makemigrations```
- ### Aplicar migraciones

  ```python manage.py migrate```

## 🔂 Paso 8: Ejecutar el Servidor de Desarrollo

```python3 -m http.server 8000```

## 🌐 Paso 9: Acceder a la Aplicación

Ir al navegador:

```http://3.144.32.107:8000/PaginaInicial.html```

## 🛑 Paso 10: Detener el Servidor

Presiona Ctrl + C en la terminal o utilizar el comando ``pkill -f "http.server``

# ⚙️ Automatización con GitHub Actions

### A continuación, se describen los pasos realizados para la configuración de un flujo de automatización inicial con GitHub Actions:

### 1. Preparación del Repositorio Existente

- Se utilizó el repositorio creado en el paso anterior.
- Se agregó una prueba / validación básica en JavaScript.
  ``` 
  describe('Basic Math Tests', () => { 
  test('basic arithmetic should work', () => { 
    expect(1 + 1).toBe(2); 
    expect(2 * 3).toBe(6); 
  }); 
  }); ``` 
- Se verificó la presencia del archivo de dependencias package.json.
  ```
  {
    "name": "my-app-tests",
    "scripts": {
    "test": "jest"
    },
    "devDependencies": {
    "jest": "^29.0.0",
    "jest-environment-jsdom": "^29.0.0"
    },
    "jest": {
    "testEnvironment": "jsdom"
    }
  }
  ```
### 2. Configuración Básica de GitHub Actions

- Se creó la carpeta .github/workflows/ y se crea el archivo .yml con la siguiente estructura.
  ```
  name: JavaScript CI

    on:
        push:
            branches: [main]

    jobs:
    test:
        runs-on: ubuntu-latest
        steps:
        - name: Checkout repository
            uses: actions/checkout@v3

        - name: Setup Node.js
            uses: actions/setup-node@v3
            with:
            node-version: '18'

        - name: Install dependencies
            run: npm install

        - name: Run tests
            run: npm test

        - name: Validate HTML structure
            run: |
            if [ ! -f "PaginaInicial.html" ]; then
            echo "Error: HTML file not found"
            exit 1
            fi
            echo "HTML validation passed"

  ```
- Se configuraron validaciones básicas sobre HTML, CSS y JavaScript.
- Se añadió un badge de estado en el archivo README.md para mostrar los resultados de la automatización.![alt text](/Imagenes/image.png)
 
        ```![JavaScript CI](https://github.com/Alexandra510R/Recetario/workflows/JavaScript%20CI/badge.svg)``` 

# Comprobación funcionamiento workflow
![alt text](/Imagenes/image-1.png)

# 📚 ¿Que es y que hace workflow?

__El workflow__ automatiza tareas dentro del repositorio.
En este caso, se ejecuta cada vez que se suben cambios y se encarga de:

Descargar el proyecto.

Validar que los archivos (HTML, CSS, JS) no tengan errores básicos.

Ejecutar pruebas definidas en la carpeta test/.

Mostrar en GitHub si la ejecución fue exitosa ✅ o si hubo errores ❌ mediante un badge en el README.md.

#  Erores encontrados al momento de la implementación

### 1. Error de sintaxis en archivo .yml

![](/Imagenes/error1.png)

__Causa:__ Uso incorrecto de tabuladores en la estructura del archivo, lo cual no es soportado por YAML.

__Solución:__ Se corrigió la sintaxis reemplazando los tabuladores por espacios, garantizando la correcta indentación del archivo.

### 2. Error: No se localizó el repositorio
![](/Imagenes/error2.png)

__Causa:__ El workflow no logró resolver la acción htmllint/htmllint-action debido a que no se encontraba el repositorio especificado o la ruta definida era incorrecta.

__Solución:__ Se modificó el código del workflow, reemplazando la referencia incorrecta a src/index.html por la ruta real del archivo en el repositorio: PaginaInicial.html.


# 🐳 Containerización con Docker

La containerización consiste en empaquetar una aplicación junto con sus dependencias dentro de un contenedor.
En este proyecto utilizamos Docker para crear una imagen ligera que incluye Nginx y los archivos estáticos de la aplicación (HTML, CSS y JavaScript).

__🔹 Beneficios__

Portabilidad: el contenedor funciona en cualquier máquina que tenga Docker.

Aislamiento: no depende de la configuración del sistema anfitrión.

Reproducibilidad: el mismo Dockerfile asegura que el entorno sea siempre idéntico.

Escalabilidad: se pueden crear múltiples instancias fácilmente.

## ⚙️ Requisitos previos para Docker Desktop en Windows

* Docker instalado en tu máquina. Puedes obtenerlo desde: [Instalar Docker](https://docs.docker.com/get-started/get-docker/)
* Docker Desktop (Windows):
  - Windows 10/11 Pro, Enterprise o Education (para usar WSL 2 o Hyper-V).
  - WSL 2 habilitado (Subsistema de Windows para Linux).
  - Virtualización activada.
  
__⚠️ Nota: En Windows Home, Docker Desktop funciona únicamente con WSL 2, por lo que es necesario habilitarlo antes de la instalación.__


## 🛠️ Construcción de la imagen

Ejecuta en la raíz del proyecto:

``` docker build -t recetario . ```

Este comando:

* Construye la imagen a partir del Dockerfile.
* Copia los archivos de src/ a la carpeta de Nginx dentro del contenedor.
* Expone el puerto 80 para servir la aplicación.

## ▶️ Ejecución del contenedor

Corre el contenedor mapeando el puerto 8080 del host al puerto 80 del contenedor:

``` docker run -d -p 8080:80 recetario ```

Este comando:

* Construye el Docker
* Crea el puerto teniendo en cuenta la imagen creada
* Permite desde Docker Desktop ingresar a la pagina web

## 🌐 Acceso a la aplicación

Una vez el contenedor esté en ejecución, accede en tu navegador a:

👉 http://localhost:8080

## ⚖️ Comparación antes/después de containerizar

| Aspecto    | Antes (sin contenedor) | Después (con Docker)  |
|-----------|------|-----------|
| Configuración del entorno | Requiere instalar Nginx manualmente y configurar rutas.   | Un Dockerfile define todo el entorno automáticamente.   |
| Portabilidad | Depende del sistema operativo y de configuraciones locales.  | Funciona en cualquier máquina con Docker. |
| Consistencia     | Puede variar entre desarrollo, pruebas y producción.  | El contenedor asegura que siempre sea el mismo entorno.  |
| Tiempo de despliegue     | Lento, requiere instalar dependencias.   | Rápido, solo se construye y corre el contenedor.  |
| Escalabilidad     | Compleja, requiere configurar varios servidores.  | Simple, basta con correr más contenedores.  |


# 📊 Resultados Obtenidos

- ✅ Creación de la instancia de manera correcta
- ✅ Creación del repositorio en GitHub
- ✅ Desarrollo del aplicativo web Recetario
- ✅ Implementación de un formulario funcional con validación
- ✅ Despliegue exitoso del aplicativo en la instancia
- ✅ Creacion de workflow
- ✅ Automatización con GitHub Actions
- ✅ Containerización con Docker
