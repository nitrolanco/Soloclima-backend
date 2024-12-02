# API Simple con FastAPI

API desarrollada con FastAPI que se conecta a una base de datos MongoDB. Asegúrate de tener la base de datos alojada y configura el archivo `.env`.

## Requisitos

- Python 3.7+
- MongoDB (por ejemplo, MongoDB Atlas)

## Instalación

1. Clona el repositorio y navega al proyecto:
   ```bash
   git clone <url-del-repositorio>
   cd <directorio-del-proyecto>
   ```

````

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura tu URI de MongoDB en el archivo `.env`:
   ```ini
   MONGODB_URI=mongodb://<usuario>:<contraseña>@<servidor>:<puerto>/<base-de-datos>
   ```

## Ejecutar

Lanza el servidor con:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`.

## Estructura

```
.
├── app
│   └── main.py
├── requirements.txt
└── .env
```

````
