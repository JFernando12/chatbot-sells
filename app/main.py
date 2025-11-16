import uvicorn
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

from app.app import app

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )