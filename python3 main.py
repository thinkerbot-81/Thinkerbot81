from telegram.ext import Updater, CommandHandler
from config import BOT_TOKEN

def start(update, context):
    update.message.reply_text("Bot chal raha hai!")

def main():
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN missing")
        return

    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
