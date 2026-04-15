# 🚀 Sistema de Gestión de Usuarios Flask

## 📋 Descripción General

Sistema completo de gestión de usuarios desarrollado en Flask con características empresariales avanzadas, incluyendo autenticación segura, panel de administración, intranet corporativa, sistema de backup y gestión de políticas de seguridad.

---

## 🚀 Cómo ponerlo en marcha

### 1️⃣ Crear un entorno virtual

```bash
cd user_manager_flask_v2
python -m venv venv
```

---

### 2️⃣ Activar el entorno virtual

🪟 **Windows:**
```bash
venv\Scripts\activate
```

🐧 **Linux / macOS:**
```bash
source venv/bin/activate
```

---

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Ejecutar la aplicación

```bash
python run.py
```

Luego abre tu navegador en 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 5️⃣ Desactivar el entorno virtual

```bash
deactivate
```

---

## 📁 Estructura del proyecto

```
user_manager_flask_v2/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── utils/
│   │   └── security.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── register.html
│       ├── login.html
│       └── admin.html
│
├── run.py
├── requirements.txt
└── README.md
```

---

## 🧩 Tecnologías utilizadas

- **Flask** – Framework principal.
- **Flask-Login** – Manejo de sesiones seguras.
- **Flask-WTF** – Formularios y protección CSRF.
- **Flask-SQLAlchemy** – ORM para SQLite.
- **pyotp** – Generación y validación de códigos 2FA.
- **Bootstrap 5** – Interfaz moderna y responsive.

---

