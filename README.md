# ☁️ Cloud Calculator

![GitHub repo size](https://img.shields.io/github/repo-size/TU_USUARIO/cloud-calculator?style=flat-square)
![GitHub contributors](https://img.shields.io/github/contributors/TU_USUARIO/cloud-calculator?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/TU_USUARIO/cloud-calculator?style=flat-square)
![GitHub license](https://img.shields.io/github/license/TU_USUARIO/cloud-calculator?style=flat-square)

Aplicación web en **Python (Flask)** que funciona como una **calculadora en la nube**, con dos funcionalidades integradas:

1. 🔢 **Calculadora básica**: suma, resta, multiplicación y división.  
2. 🌡️ **Conversión de temperaturas**: Celsius ↔ Fahrenheit.  

Desplegada en la nube usando **AWS Elastic Beanstalk**.

---

## 🌐 URL de la aplicación desplegada
(Running on http://10.59.35.170:5000)(*Running on http://127.0.0.1:5000)

---

## ⚡ Tecnologías utilizadas

* **Python 3.12**
* **Flask 3.0**
* **HTML5 + CSS3**
* **AWS Elastic Beanstalk**
* **Git / GitHub**

---

## 📝 Descripción de la aplicación

La aplicación ofrece una interfaz sencilla y moderna donde el usuario puede:

- Realizar operaciones matemáticas básicas desde el navegador.
- Convertir temperaturas entre escalas Celsius y Fahrenheit.
- Ver resultados en tiempo real dentro de un panel web con estilo profesional.

---

## 📋 Requisitos previos

- Cuenta en **AWS** con acceso a **Elastic Beanstalk**.  
- **Python 3.9+** instalado en tu PC.  
- **Git** instalado.  
- **AWS CLI** y **EB CLI** configuradas con tus credenciales.  

---

## 🛠 Paso a paso del despliegue

### 1️⃣ Clonar el proyecto

```bash
git clone https://github.com/iancardonag/cloud-calculator.git
cd cloud-calculator


---

### 2️⃣ Actualizar sistema

```bash
sudo apt update
sudo apt upgrade -y
```

---

### 3️⃣ Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

pip install -r requirements.txt


---


Si ya estaba clonado:

```bash
git pull origin main
```

---

### 6️⃣ Probar en local

```
python app.py
```

---

### 7️⃣ Construir versión para producción

```bash
npm run build
```

* Esto genera la carpeta `dist` con los archivos estáticos.

**Problema frecuente:**

* Error `Cannot find module @rollup/rollup-linux-x64-gnu` al ejecutar `npm run build`.
  **Solución:**

**Problema frecuente:**

* `dist` no existía porque `npm run build` falló previamente.
  **Solución:** Limpiar `node_modules` y `package-lock.json` y reinstalar dependencias.

---

### 9️⃣ Verificar funcionamiento

* Abrir en navegador: `http://<IP_PUBLICA>/`
* Asegurarse de que el Security Group permita el puerto 80.
* Si no carga, revisar que `sudo ufw status` muestre que está inactivo o que permita HTTP.

---

## ⚠ Problemas encontrados y soluciones

| Problema                                         | Solución                                                                       |
| ------------------------------------------------ | ------------------------------------------------------------------------------ |
| La app no inicia en AWS. | Verificar que el archivo requirements.txt contenga Flask.    |
| Error "port already in use" en local | Cambiar puerto en app.run(port=5001) |
| Página no visible desde otros dispositivos.       | Configurar Security Group y verificar puertos abiertos en AWS y UFW.           |
| No se ve la página desde otros dispositivos.  | Revisar configuración de seguridad en AWS (puerto 80 abierto a 0.0.0.0/0). |

---

