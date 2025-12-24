import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("8500112291:AAEji1yU5sks3Sd10f28yCg05iIYSxHuypo)

def start(update, context):
    update.message.reply_text(
        "Assalomu alaykum!\nBot 24/7 ishlamoqda 🙂"
    )

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
