from telegram.ext import Updater, CommandHandler

# Apna bot token yahan daalein
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

def start(update, context):
    update.message.reply_text("Hello! Main aapka bot hoon.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    print("Bot chaloo ho gaya...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
