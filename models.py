from pydantic import BaseModel

class ChatResponse(BaseModel):
    prompt: str