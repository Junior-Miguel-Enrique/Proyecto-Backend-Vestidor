# Configuración de Variables de Entorno - Backend

Guía detallada de las variables requeridas en el archivo `.env` para la ejecución del servidor FastAPI.

---

## 🔑 Variables Esenciales

| Variable | Tipo | Descripción | Ejemplo / Default |
| :--- | :--- | :--- | :--- |
| `PROJECT_NAME` | String | Nombre del sistema | `Vestidor Virtual API` |
| `ENVIRONMENT` | String | Entorno (`development`, `production`, `testing`) | `development` |
| `SECRET_KEY` | String | Llave criptográfica para firmas JWT | Cadena segura de 64 caracteres |
| `ALGORITHM` | String | Algoritmo de firma de tokens | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Int | Duración del token de sesión en minutos | `60` |

---

## 🗄️ Base de Datos (PostgreSQL)

| Variable | Descripción | Formato de Conexión |
| :--- | :--- | :--- |
| `DATABASE_URL` | URI de conexión SQLAlchemy | `postgresql://usuario:password@localhost:5432/nombre_db` |

---

## 🤖 Servicios Externos e Inteligencia Artificial

| Variable | Proveedor | Finalidad |
| :--- | :--- | :--- |
| `GEMINI_API_KEY` | Google AI Studio | Modelos multimodales para análisis de prendas y recomendaciones |
| `PAYPAL_CLIENT_ID` | PayPal Developer | Procesamiento de pagos en checkout |
| `PAYPAL_CLIENT_SECRET`| PayPal Developer | Autenticación OAuth2 para transacciones |
| `AWS_S3_BUCKET` | AWS / MinIO | Almacenamiento seguro de fotografías del vestidor virtual |
