from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from utils import BOT_TOKEN, WEBHOOK_URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot hoạt động thành công!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_webhook(
    listen="0.0.0.0",
    port=10000,
    webhook_url=WEBHOOK_URL
)
