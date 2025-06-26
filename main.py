from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "7577180489:AAHkY3lioHL1_M2q_bPGoQJNaZa4JNyn0LU")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Chào mừng bạn đến với bot hỗ trợ tài liệu")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    app.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url="https://file-and-code.onrender.com"
    )
