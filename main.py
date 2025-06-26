
import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

TOKEN = os.getenv("BOT_TOKEN", "7577180489:AAHkY3lioHL1_M2q_bPGoQJNaZa4JNyn0LU")
WEBHOOK_URL = "https://file-and-code.onrender.com"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot hoạt động bình thường!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Thiết lập webhook
    async def set_webhook():
        await app.bot.set_webhook(url=WEBHOOK_URL)
        logger.info(f"✅ Webhook đã thiết lập: {WEBHOOK_URL}")

    app.add_handler(CommandHandler("start", start))

    # Chạy bot bằng webhook, không cần mở cổng (do Render sẽ tự giữ alive)
    app.run_webhook(
        listen="0.0.0.0",
        port=443,
        webhook_url=WEBHOOK_URL,
        on_startup=set_webhook
    )

if __name__ == "__main__":
    main()
