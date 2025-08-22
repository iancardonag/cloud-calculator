# ☁️ Cloud Calculator

![GitHub repo size](https://img.shields.io/github/repo-size/iancardonag/cloud-calculator?style=flat-square)  
![GitHub contributors](https://img.shields.io/github/contributors/iancardonag/cloud-calculator?style=flat-square)  
![GitHub last commit](https://img.shields.io/github/last-commit/iancardonag/cloud-calculator?style=flat-square)  
![GitHub license](https://img.shields.io/github/license/iancardonag/cloud-calculator?style=flat-square)  

Aplicación web en **Python (Flask)** que funciona como una **calculadora en la nube**, con dos funcionalidades integradas:

1. 🔢 **Calculadora básica**: suma, resta, multiplicación y división.  
2. 🌡️ **Conversión de temperaturas**: Celsius ↔ Fahrenheit.  

Desplegada en la nube usando **AWS EC2 con Nginx + Gunicorn**.

---

## 🌐 URL de la aplicación desplegada
👉 `http://<IP_PUBLICA_EC2>/`

*(Reemplazar con la IP pública de tu instancia EC2)*

---

## ⚡ Tecnologías utilizadas

* **Python 3.12**
* **Flask 3.0**
* **Gunicorn** (servidor de producción WSGI)
* **Nginx** (servidor web / reverse proxy)
* **HTML5 + CSS3**
* **AWS EC2**
* **Git / GitHub**

---

## 📝 Descripción de la aplicación

La aplicación ofrece una interfaz sencilla y moderna donde el usuario puede:

- Realizar operaciones matemáticas básicas desde el navegador.  
- Convertir temperaturas entre escalas Celsius y Fahrenheit.  
- Ver resultados en tiempo real dentro de un panel web con estilo profesional.  

---

## 📋 Requisitos previos

- Cuenta en **AWS** con acceso a **EC2**.  
- **Instancia Ubuntu 22.04** creada en EC2.  
- **Puertos abiertos en Security Groups**:  
  - **22 (SSH)** → acceso remoto.  
  - **80 (HTTP)** → acceso web.  
- **Clave .pem descargada** para conexión SSH.  
- **Git** y **Python 3.9+** instalados en la instancia.  

---

## 🛠 Paso a paso del despliegue en EC2

### 1️⃣ Conectarse a la instancia
```bash
---
ssh -i tu_clave.pem ubuntu@<IP_PUBLICA_EC2>

### 2️⃣ Instalar dependencias del sistema
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv nginx git -y

### 3️⃣ Clonar el proyecto
git clone https://github.com/iancardonag/cloud-calculator.git
cd cloud-calculator

###4️⃣ Crear entorno virtual e instalar dependencias
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn

###5️⃣ Probar aplicación localmente
python app.py
Verificar que funciona en http://127.0.0.1:5000 (dentro de la instancia).

⚙️ Configuración de Gunicorn + Nginx

### 6️⃣ Ejecutar Gunicorn
gunicorn app:app --bind 127.0.0.1:5000

### 7️⃣ Configurar Nginx
Crear archivo de configuración:
sudo nano /etc/nginx/sites-available/flaskapp

Contenido:
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

Enlazar y eliminar el default:
sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx

### 🔄 Automatizar con systemd
sudo nano /etc/systemd/system/flaskapp.service

Contenido:
[Unit]
Description=Gunicorn instance to serve Flask app
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/cloud-calculator
Environment="PATH=/home/ubuntu/cloud-calculator/venv/bin"
ExecStart=/home/ubuntu/cloud-calculator/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:5000 app:app

[Install]
WantedBy=multi-user.target

### Activar servicio:
sudo systemctl daemon-reload
sudo systemctl enable flaskapp
sudo systemctl start flaskapp

### verificar:
sudo systemctl status flaskapp


🛑 Apagar para no generar costos
Detener la instancia (recomendado):
Desde AWS Console → EC2 → Detener instancia.
Esto no borra nada, solo detiene cobros de cómputo.

Terminar la instancia (destruirla):
Desde AWS Console → EC2 → Terminar instancia.
Esto borra todo permanentemente.

| Problema                                       | Solución                                                                                         |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Página de Nginx por defecto en lugar de la app | Eliminar `/etc/nginx/sites-enabled/default`                                                      |
| App no visible desde navegador                 | Revisar que Security Group tenga puerto 80 abierto a `0.0.0.0/0`                                 |
| Error "No module named flask"                  | Instalar dependencias en el entorno: `pip install -r requirements.txt`                           |
| App no arranca tras reinicio                   | Verificar con `sudo systemctl status flaskapp` y reiniciar con `sudo systemctl restart flaskapp` |
