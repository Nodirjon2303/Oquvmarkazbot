from Buttons import *
from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')