from fastapi import APIRouter, HTTPException
from app.telegram_bot import application

router = APIRouter()

@router.get("/send_message")
async def send_message():
    print("send messsage")
    return {"status": "Message sent successfully"}