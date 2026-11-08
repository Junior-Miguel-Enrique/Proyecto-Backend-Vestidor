# Matriz de Seguridad y Roles (RBAC) - Vestidor Virtual

Definición de políticas de control de acceso basadas en roles (Role-Based Access Control) y permisos por endpoint.

---

## 👥 Roles del Sistema

1. **SUPERADMIN:** Acceso global a tenants, configuración de plataforma y auditorías.
2. **BRANCH_ADMIN:** Administración de catálogo de sucursal, stock de prendas y reportes locales.
3. **SALES_CLERK:** Atención de ventas, validación de reservas y entregas de probador virtual.
4. **CUSTOMER:** Usuario final cliente (catálogo, reservas, favoritos, checkout y probador virtual).

---

## 🛡️ Matriz de Permisos por Módulo

| Módulo | Endpoint / Recurso | CUSTOMER | SALES_CLERK | BRANCH_ADMIN | SUPERADMIN |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Auth** | `/api/v1/auth/login` | ✅ | ✅ | ✅ | ✅ |
| **Catalog** | `/api/v1/products` (GET) | ✅ | ✅ | ✅ | ✅ |
| **Catalog** | `/api/v1/products` (POST/PUT/DELETE) | ❌ | ❌ | ✅ | ✅ |
| **Virtual Try-On** | `/api/v1/ai/try-on` | ✅ | ✅ | ✅ | ✅ |
| **Reservations** | `/api/v1/reservations` (Mis reservas) | ✅ | ✅ | ✅ | ✅ |
| **Reservations** | `/api/v1/reservations` (Validar/Confirmar) | ❌ | ✅ | ✅ | ✅ |
| **Analytics** | `/api/v1/analytics/voice-reports` | ❌ | ❌ | ✅ | ✅ |
| **Audit Logs** | `/api/v1/audit-logs` | ❌ | ❌ | ❌ | ✅ |

---

## 🔒 Especificación de Tokens JWT

- **Algoritmo:** HMAC-SHA256 (`HS256`)
- **Claims Requeridos:** `sub` (ID usuario), `role` (Rol asignado), `exp` (Expiración), `iat` (Emisión).
- **Rotación:** Invalidación en logout y caducidad automática a los 60 minutos.
