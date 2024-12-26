from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
print("Bot token:", BOT_TOKEN)

application = Application.builder().token(BOT_TOKEN).build()

# Handlers
async def start_command(update: Update, context):
    await update.message.reply_text("Welcome to the Telegram Mini App!")

async def echo_message(update: Update, context):
    await update.message.reply_text(f"You said: {update.message.text}")

# Add Handlers
application.add_handler(CommandHandler("start", start_command))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))
