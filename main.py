
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("9027336241:AAEUc0DToFtysl71Fhs-3ellHFf2cHBMSOk")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚽ أهلاً بك في MatchMind AI\n\n"
        "بوت إحصائيات وتحليل كرة القدم.\n"
        "استخدم /help لمعرفة الأوامر."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 أوامر MatchMind AI:\n\n"
        "/start - تشغيل البوت\n"
        "/help - المساعدة"
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is missing from environment variables")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("MatchMind AI is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
