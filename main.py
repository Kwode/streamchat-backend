from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai import chat_response
from fastapi.responses import StreamingResponse
from models import ChatResponse


app = FastAPI()

origins = [
    "https://streamchat-frontend.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_methods = ['*']
)

@app.post('/chat')
def chat(request: ChatResponse):
    return StreamingResponse(
        chat_response(prompt=request.prompt),
        media_type='text/plain'
    )
