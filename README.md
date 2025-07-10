# 🏓 Proyecto Base de Datos: SQLAlchemy + Alembic + PostgreSQL

Angel Vargas, Denisse Maldonado, Christopher Navarrete 

Este proyecto utiliza **SQLAlchemy** como ORM y **Alembic** para migraciones, conectando a una base de datos **PostgreSQL**.  
Incluye estructura para una API con **FastAPI** y ejemplos de CRUD.

---

## 🚀 Guía Rápida de Instalación

### 1. Clona el repositorio

```bash
git clone <URL_DEL_REPO>
cd Basededatos
```

---

### 2. Crea y activa un entorno virtual

**Windows:**
```bash
python -m venv env
.\env\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv env
source env/bin/activate
```

---

### 3. Copia y configura el archivo de entorno

```bash
cp sample.env .env
```

Edita `.env` y ajusta la variable `DATABASE_URI` con tus datos de PostgreSQL:

```
DATABASE_URI=postgresql://usuario:password@localhost:5432/mi_base
```

---

### 4. Instala las dependencias

```bash
pip install -r requirements.txt
```

---

### 5. Inicializa la base de datos con Alembic

```bash
alembic revision --autogenerate -m "primer modelo"
alembic upgrade head
```

---

### 6. Ejecuta el servidor FastAPI

```bash
uvicorn app.main:app --reload
```

Abre tu navegador en: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para ver la documentación interactiva.

---

## 📁 Estructura de Archivos Importantes

- `.env`: configuración local (no subir al repo)
- `sample.env`: plantilla para `.env`
- `requirements.txt`: dependencias del proyecto
- `app/models.py`: define tus modelos SQLAlchemy
- `app/db.py`: conexión y base de datos
- `app/routers/`: rutas de la API (FastAPI)
- `app/cruds/`: lógica CRUD para cada modelo
- `alembic/versions/`: migraciones generadas

---

## 📝 Notas útiles

- Las migraciones se guardan en `alembic/versions/`.
- Para deshacer una migración:
  ```bash
  alembic downgrade -1
  ```
- Para crear nuevas migraciones tras modificar modelos:
  ```bash
  alembic revision --autogenerate -m "mensaje"
  alembic upgrade head
  ```
- Puedes probar la API desde `/docs` o `/redoc` en el navegador.

---

## 💡 Consejos

- Mantén tu archivo `.env` fuera del control de versiones.
- Si tienes problemas de conexión, revisa que PostgreSQL esté corriendo y los datos de `.env` sean correctos.
- Usa entornos virtuales para evitar conflictos de dependencias.

---

¡Listo! Ya puedes comenzar a desarrollar tu proyecto con SQLAlchemy, Alembic y FastAPI.
