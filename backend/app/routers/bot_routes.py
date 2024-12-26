from fastapi import APIRouter, HTTPException
from app.telegram_bot import application

router = APIRouter()

@router.get("/send_message")
async def send_message(chat_id: int, text: str):
    try:
        # Directly use PTB's bot instance to send a message
        await application.current.bot.send_message(chat_id=chat_id, text=text)
        return {"status": "Message sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
