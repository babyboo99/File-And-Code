import os
from telegram.ext import ApplicationBuilder
from src.handlers import register_handlers

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

async def on_start(app):
    print("✅ Bot khởi động thành công.")
    await app.bot.set_webhook(url=WEBHOOK_URL)

if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    register_handlers(application)

    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", "8443")),
        webhook_url=WEBHOOK_URL,
        on_startup=on_start
    )