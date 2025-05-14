from fastapi import FastAPI
from models import MessageRequest, MessageResponse
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("API_KEY"))
app = FastAPI()

@app.post("/message", response_model=MessageResponse)
def read_item(message: MessageRequest):
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=message.content
    )
    return {
        "response": response.text
    }