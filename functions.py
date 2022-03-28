from Buttons import *
from telegram import Update
from telegram.ext import CallbackContext
from Database import *

state_main = 1


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name}\n'
                              f"Zako o'quv markazimizning botiga xush kelibsiz", reply_markup=main_button())
    if checkuser(update.effective_user.id):
        add_user(update.effective_user.first_name, update.effective_user.last_name, f"{update.effective_user.id}")
        print("bazaga saqlandi")
    return state_main


def command_kurslar(update: Update, context: CallbackContext):
    update.message.reply_text("Bizning kurslar", reply_markup=ReplyKeyboardRemove())
    data = get_course_name()
    print(data)


def command_ustozlar(update: Update, context: CallbackContext):
    update.message.reply_text("Bizning Ustozlar")


def command_biz(update: Update, context: CallbackContext):
    update.message.reply_text("Biz haqimizda")
