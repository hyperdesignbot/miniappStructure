from telegram import Update
from app.utils.tghelper.keyboards import key_web_app

async def start_command(update: Update, context):
    """Send a message with a button that opens a the web app."""

    await update.message.reply_text(
        text="برای شروع دکمه ی زیر را بزنید",
        reply_markup=key_web_app,
    )
