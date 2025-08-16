
import os
from telegram.ext import Updater, CommandHandler
import logging

# Telegram Bot Setup
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

logging.basicConfig(level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=CHAT_ID, text="🚀 Bot is running successfully!")

if __name__ == "__main__":
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
