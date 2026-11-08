# Vestidor Virtual Inteligente - Backend API

API REST empresarial construida con **FastAPI**, **SQLAlchemy** y **PostgreSQL** para la plataforma de Vestidor Virtual y E-Commerce con Inteligencia Artificial.

---

## 🏛️ Arquitectura del Sistema

El backend sigue una arquitectura modular en capas basada en estándares modernos de Python:

```
app/
├── api/             # Capa de presentación y controladores de la API
│   ├── deps.py      # Inyección de dependencias (sesión DB, usuario autenticado)
│   └── v1/          # Endpoints versionados (auth, productos, reservas, pagos, IA)
├── core/            # Reglas de negocio y lógica de dominio (transacciones, políticas)
├── models/          # Modelos de base de datos ORM (SQLAlchemy)
├── schemas/         # Esquemas de validación y DTOs (Pydantic v2)
├── ml/              # Modelos de aprendizaje automático y algoritmos de recomendación
└── config.py        # Configuración centralizada basada en variables de entorno
```

---

## 🚀 Tecnologías Principales

- **Framework:** FastAPI (Python 3.11+)
- **ORM & Migraciones:** SQLAlchemy 2.0 & Alembic
- **Base de Datos:** PostgreSQL
- **Seguridad:** JWT (JSON Web Tokens) con bcrypt y hashing seguro
- **IA & Try-On:** Google Gemini API y Gradio Client para probador virtual de prendas
- **Testing:** Pytest con soporte asíncrono (`pytest-asyncio`)
- **Contenedores:** Dockerfile & Procfile para despliegue en la nube

---

## ⚙️ Requisitos Previos

- Python 3.11 o superior
- Servidor PostgreSQL activo
- Gestor de paquetes `pip` o entorno virtual `venv`

---

## 📦 Instalación y Configuración

1. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno:**
   Copia el archivo `.env.example` a `.env` y ajusta los valores de conexión:
   ```bash
   cp .env.example .env
   ```

4. **Ejecutar migraciones de base de datos:**
   ```bash
   alembic upgrade head
   ```

5. **Iniciar el servidor de desarrollo:**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

---

## 📖 Documentación Interactiva de la API

Una vez iniciado el servidor, puedes acceder a la documentación Swagger y Redoc generada automáticamente:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

## 🧪 Ejecución de Pruebas

Para ejecutar la suite de pruebas unitarias y de integración:

```bash
pytest
```
