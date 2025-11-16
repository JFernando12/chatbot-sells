from fastapi import APIRouter

from app.graph.graph import graph

chat_router = APIRouter()

@chat_router.post("/")
async def send(message: str):
    initial_state = {"query": message}
    result = graph.invoke(initial_state)
    return {"response": result.get("response", "Sorry, I don't have an answer for that.")}
