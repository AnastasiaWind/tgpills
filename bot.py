import os
from datetime import time, timezone, timedelta

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = int(os.environ["CHAT_ID"])
BUTTON_DATA = "btn_1"

async def send_daily(context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Нажми меня", callback_data=BUTTON_DATA)]
    ])
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="Ежедневный текст",
        reply_markup=keyboard,
    )

async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text("Текст после нажатия")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CallbackQueryHandler(on_button, pattern=f"^{BUTTON_DATA}$"))

    msk = timezone(timedelta(hours=3))
    app.job_queue.run_daily(send_daily, time=time(9, 0, tzinfo=msk))

    app.run_polling()

if __name__ == "__main__":
    main()
