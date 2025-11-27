from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat")
async def generate_chat_response(body: ChatRequest):

