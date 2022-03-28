
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters
from functions import *




updater = Updater('5277163960:AAEsmEbHiy_dEle45YcU61Welo0YBQOimGI')

conv = ConversationHandler(
    entry_points=[
        CommandHandler('start', start)
    ],
    states={
        state_main:[
            MessageHandler(Filters.regex('^(' + bizningkurslar + ')$'), command_kurslar),
            MessageHandler(Filters.regex('^(' + bizning_ustozlar + ')$'), command_ustozlar),
            MessageHandler(Filters.regex('^(' + biz_haqimizda + ')$'), command_biz)
        ]

    },
    fallbacks=[
        CommandHandler('start', start)
    ]
)


updater.dispatcher.add_handler(conv)

updater.start_polling()
updater.idle()
