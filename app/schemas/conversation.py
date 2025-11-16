from pydantic import BaseModel

class Conversation(BaseModel):
    user_id: str