from pydantic import BaseModel

class Message(BaseModel):
    role: str
    content: str
    conversation_id: str
    created_at: str