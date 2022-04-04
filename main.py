from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters, \
    CallbackQueryHandler
from functions import *

# import logging
#
# logging.basicConfig(
#         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#         level=logging.DEBUG)


updater = Updater('5277163960:AAEsmEbHiy_dEle45YcU61Welo0YBQOimGI')

conv = ConversationHandler(
    entry_points=[
        CommandHandler('start', start)
    ],
    states={
        state_main: [
            MessageHandler(Filters.regex('^(' + bizningkurslar + ')$'), command_kurslar),
            MessageHandler(Filters.regex('^(' + bizning_ustozlar + ')$'), command_ustozlar),
            MessageHandler(Filters.regex('^(' + biz_haqimizda + ')$'), command_biz)
        ],
        state_courses: [
            CallbackQueryHandler(command_courses)
        ],
        state_kurs_detail: [
            CallbackQueryHandler(command_kurs_detail)
        ],
        state_kurs_ism: [
            MessageHandler(Filters.text, command_kurs_ism)
        ],
        state_kurs_raqam: [
            MessageHandler(Filters.contact, command_kurs_raqam),
            MessageHandler(Filters.text, command_kurs_raqam_text)
        ],
        state_teacher_kurs: [
            CallbackQueryHandler(command_teacher_kurs)
        ],
        7: [
            MessageHandler(Filters.regex('^(' + "Kurs qo'shish" + ')$'), command_add_kurs),
            MessageHandler(Filters.regex('^(' + "O'qituvchi qo'shish" + ')$'), command_add_teacher)
        ],
        'state_kurs_name': [
            MessageHandler(Filters.text, command_kurs_name)
        ],
        'state_kurs_narxi': [
            MessageHandler(Filters.text, command_kurs_narxi)
        ],
        'state_kurs_duration': [
            MessageHandler(Filters.text, command_kurs_duration)
        ],
        'state_kurs_amaliyot': [
            MessageHandler(Filters.text, command_kurs_amaliyot)
        ],
        'state_kurs_technology': [
            MessageHandler(Filters.text, command_kurs_technology)
        ],
        'state_kurs_time': [
            MessageHandler(Filters.text, command_kurs_time)
        ]

    },
    fallbacks=[
        CommandHandler('start', start)
    ]
)

updater.dispatcher.add_handler(conv)

updater.start_polling()
updater.idle()
