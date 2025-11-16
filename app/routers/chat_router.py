from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.chat_service import chat_service

chat_router = APIRouter()

@chat_router.post("/")
async def send(message: str):
    response = chat_service.send(message)
    
    return JSONResponse(content={"response": response})