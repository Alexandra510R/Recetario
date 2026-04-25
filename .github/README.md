# ☁️ Despliegue en AWS EC2

Documentación del proceso de despliegue de la aplicación **Recetario** en una instancia EC2 de Amazon Web Services.

---

## 🖥️ Configuración de la Instancia

| Parámetro | Valor |
|-----------|-------|
| **Nombre** | Recetario |
| **AMI** | Ubuntu Server 24.04 LTS |
| **Tipo** | t3.micro |
| **Almacenamiento** | 8 GB gp3 |
| **IP Pública** | 3.18.225.21 |

---

## 🔒 Grupo de Seguridad (Firewall)

Se configuró el grupo de seguridad `recetario-sg` con las siguientes reglas de entrada:

| Tipo | Protocolo | Puerto | Origen |
|------|-----------|--------|--------|
| SSH | TCP | 22 | 0.0.0.0/0 |
| HTTP | TCP | 80 | 0.0.0.0/0 |
| HTTPS | TCP | 443 | 0.0.0.0/0 |
| TCP Personalizado | TCP | 8000 | 0.0.0.0/0 |

---

## 🔑 Conexión SSH desde Windows

Para conectarse a la instancia desde Windows usando PowerShell:

**1. Configurar permisos del archivo `.pem`** (ejecutar como Administrador):

```powershell
$pemFile = "RUTA\recetario-key.pem"
$acl = Get-Acl $pemFile
$acl.SetAccessRuleProtection($true, $false)
$acl.Access | ForEach-Object { $acl.RemoveAccessRule($_) }
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("TU_USUARIO","Read","Allow")
$acl.AddAccessRule($rule)
Set-Acl $pemFile $acl
```

**2. Conectarse al servidor:**

```powershell
ssh -i "RUTA\recetario-key.pem" ubuntu@3.18.225.21
```

---

## ⚙️ Preparación del Entorno

Una vez conectado al servidor, ejecutar los siguientes comandos:

**Actualizar el sistema:**
```bash
sudo apt update && sudo apt upgrade -y
```

**Instalar dependencias:**
```bash
sudo apt install python3-pip python3-venv git nodejs npm -y
```

---

## 📂 Clonar el Repositorio

```bash
git clone https://github.com/Alexandra510R/Recetario.git
cd Recetario
```

---

## 🚀 Ejecutar la Aplicación

Desde la carpeta del proyecto, iniciar el servidor HTTP de Python:

```bash
python3 -m http.server 8000
```

**Detener el servidor:**
```bash
pkill -f "http.server"
```

---

## 🌐 Acceso a la Aplicación

Una vez iniciado el servidor, la aplicación está disponible en:

| Página | URL |
|--------|-----|
| Página Principal | http://3.18.225.21:8000/src/PaginaInicial.html |
| Recetas | http://3.18.225.21:8000/src/Recetas.html |
| Registro | http://3.18.225.21:8000/src/Registro.html |

---

## 📌 Notas importantes

- El archivo `recetario-key.pem` **no debe subirse al repositorio** — está incluido en `.gitignore`.
- La IP pública puede cambiar si la instancia se detiene y se reinicia. Para una IP fija, configurar una **Elastic IP** en AWS.
- Para producción se recomienda usar **Nginx** con certificado **SSL (HTTPS)** en lugar del servidor HTTP de Python.

---