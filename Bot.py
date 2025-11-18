import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")   # 🔥 Using environment variable

WELCOME_TEXT = (
    "Assalamualaikum — Main PlayoutMaster Bot hoon.\n\n"
    "Commands:\n"
    "/start - Welcome message\n"
    "/help - Menu & quick keywords\n\n"
    "Type: vmix, obs, playout, software list"
)

HELP_TEXT = (
    "PlayoutMaster Help:\n"
    "- vmix -> vMix info\n"
    "- obs -> OBS tips\n"
    "- playout -> Playout software list\n"
    "- software list -> All supported tools"
)

SOFTWARE_LIST = {
    "vmix": "vMix — Live production software.",
    "obs": "OBS Studio — Open-source streaming.",
    "wirecast": "Wirecast — Pro streaming system.",
    "playbox": "PlayBox — TV channel playout.",
    "playout": "Playout systems supported: vMix, OBS, Wirecast, PlayBox."
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT)

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    for key in SOFTWARE_LIST:
        if key in text:
            await update.message.reply_text(SOFTWARE_LIST[key])
            return

    await update.message.reply_text(
        "Thanks! Type /help for vMix, OBS, and Playout commands."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("Bot Running 24/7...")
    app.run_polling()

if __name__ == "__main__":
    main()
