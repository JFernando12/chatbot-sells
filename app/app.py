from fastapi import FastAPI

from app.routers.chat_router import chat_router

def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(chat_router, prefix="/chat", tags=["chat"])

    return app

app = create_app()
