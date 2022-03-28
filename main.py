
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler
from functions import *




updater = Updater('5277163960:AAEsmEbHiy_dEle45YcU61Welo0YBQOimGI')

conv = ConversationHandler(
    entry_points=[
        CommandHandler('start', start)
    ],
    states={

    },
    fallbacks=[
        CommandHandler('start', start)
    ]
)


updater.dispatcher.add_handler(conv)

updater.start_polling()
updater.idle()
