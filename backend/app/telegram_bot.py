from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
from app.plugins.start_bot import start_command

application = Application.builder().token(BOT_TOKEN).build()


# Add Handlers
application.add_handler(CommandHandler("start", start_command))
