# ☁️ Cloud Calculator (Flask + AWS)

![GitHub repo size](https://img.shields.io/github/repo-size/iancardonag/cloud-calculator?style=flat-square)
![GitHub contributors](https://img.shields.io/github/contributors/iancardonag/cloud-calculator?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/iancardonag/cloud-calculator?style=flat-square)
![GitHub license](https://img.shields.io/badge/license-MIT-green?style=flat-square)

Aplicación web en **Python (Flask)** que funciona como una **calculadora en la nube**, con dos funcionalidades integradas:

1. 🔢 **Calculadora básica**: suma, resta, multiplicación y división.  
2. 🌡️ **Conversión de temperaturas**: Celsius ↔ Fahrenheit.

Pensada para desplegar en **AWS Elastic Beanstalk** (capa gratuita), manteniendo un estilo visual limpio tipo “mini-dashboard”.

---

## 📝 Descripción de la aplicación

La app ofrece una interfaz web moderna con dos tarjetas:
- **Operaciones matemáticas básicas** entre dos números.
- **Conversor de temperatura** entre °C y °F.

Los resultados se muestran en la misma página, sin recargas complejas.

---

## ⚙️ Tecnologías utilizadas

- **Python 3.12**
- **Flask 3.0**
- **Gunicorn** (servidor WSGI para producción en AWS)
- **HTML5 + CSS3**
- **AWS Elastic Beanstalk**
- **Git / GitHub**

---

## 🌐 URL de la aplicación desplegada

> Reemplaza esto con tu URL real cuando despliegues:  
> **https://TU-ENTORNO.eba-xxxxxxx.region.elasticbeanstalk.com**

---

## 🔑 Instrucciones básicas de acceso

- **Local**: `http://127.0.0.1:5000`  
- **Misma red local** (opcional): `http://<IP_LAN_DE_TU_PC>:5000`  
- **Producción (AWS EB)**: URL pública generada por Elastic Beanstalk (arriba).

---

## ✅ Requisitos previos detallados

1. **Cuenta AWS** con permisos para Elastic Beanstalk, EC2 e IAM.  
2. **AWS CLI** y **EB CLI** instaladas y configuradas:
   ```bash
   aws configure
   # Ingresa Access Key, Secret, región (ej. us-east-1) y formato (json)

pip install awsebcli
## ✅ Requirements:

Flask==3.0.0
gunicorn==21.2.0


## ✅ Clonar y preparar el entorno:
git clone https://github.com/iancardonag/cloud-calculator.git
cd cloud-calculator

python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
python app.py
# Abre http://127.0.0.1:5000 y verifica que funcione.

## Inicializar Elastic Beanstalk
eb init -p python-3.9 cloud-calculator
# Selecciona tu región (ej. us-east-1).
# Si pide crear roles, acepta (crea "aws-elasticbeanstalk-ec2-role" y service role).

## Crear entorno Single instance:
eb create cloud-calculator-env \
  --single \
  --instance_types t3.micro \
  --scale 1
# Espera a que el estado esté 'Green'.

## Actualizar la app despues de cambios:

git add .
git commit -m "Mejoras UI y fixes"
eb deploy

Configuraciones de AWS
Security Groups (entorno single instance)

Inbound (entradas) del SG de la EC2:

HTTP 80: 0.0.0.0/0 (público)

HTTPS 443 (opcional si configuras SSL): 0.0.0.0/0

SSH 22 (solo si necesitas entrar por SSH): tu IP (ej. x.x.x.x/32)

Outbound (salidas): permitir All traffic (por defecto).

Tipo de instancia

t3.micro (recomendado) o t2.micro (capa gratuita).

Variables de entorno (opcional)

En eb setenv o consola de EB:

FLASK_ENV=production

PYTHONUNBUFFERED=1

Escalado

Para pruebas académicas: 1 instancia (sin autoescalado).

| Problema                                | Causa típica                                                 | Solución                                                                                                 |
| --------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| **502 Bad Gateway**                     | La app no expone en el puerto esperado o Gunicorn no levantó | Asegura `Procfile` con `gunicorn app:app --bind 0.0.0.0:5000`. Revisa `eb logs`.                         |
| **ModuleNotFoundError: flask**          | No se instalaron dependencias en EB                          | Verifica `requirements.txt` y redeploy: `eb deploy`.                                                     |
| **La app funciona local pero no en EB** | Diferencias de entorno/puerto                                | No uses `app.run()` en producción. Deja que **Gunicorn** arranque tu app con el `Procfile`.              |
| **No carga estáticos o CSS**            | Cache o paths relativos                                      | Forzar refresh (Ctrl+F5). Revisa rutas o usa `url_for('static', filename='...')` si migras a plantillas. |
| **Timeout en despliegue**               | Red lenta/instalación pesada                                 | Reintenta `eb deploy` y revisa `eb logs` para el paquete que tarda.                                      |

Consejos y mejores prácticas aprendidas

Usa Procfile + Gunicorn para entornos productivos en EB.

Mantén un requirements.txt minimalista y bloqueado (versiones exactas).

No hardcodees el puerto en producción con app.run(); deja que lo maneje Gunicorn.

Agrega badges y capturas al README: sube tu nivel de presentación.

Limita SSH 22 a tu IP; HTTP 80 público.

Cuando actualices el código: git commit → eb deploy.

Documenta errores y soluciones en tu README (¡puntos extra en evaluación!).

##Comandos utilizados:
# Local
git clone https://github.com/iancardonag/cloud-calculator.git
cd cloud-calculator
python -m venv venv
# Win: venv\Scripts\activate   |  Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
python app.py

# AWS Elastic Beanstalk
pip install awsebcli
eb init -p python-3.9 cloud-calculator
eb create cloud-calculator-env --single --instance_types t3.micro --scale 1
eb open
eb status
eb health
eb logs

# Actualizaciones
git add .
git commit -m "Cambios"
eb deploy
