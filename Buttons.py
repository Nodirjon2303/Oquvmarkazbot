from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
bizningkurslar = 'Bizning Kurslar'
bizning_ustozlar = 'Bizning Ustozlar'
biz_haqimizda = 'Biz haqimizda'
def main_button():
        button = [
            [bizningkurslar],
            [bizning_ustozlar, biz_haqimizda]
        ]

        return ReplyKeyboardMarkup(button, resize_keyboard=True)


def course_buttons(data):
    buttons = []
    res = []
    for i in data:
        res.append(InlineKeyboardButton(i[1], callback_data=f'{i[0]}'))
        if len(res)==2:
            buttons.append(res)
            res=[]
    if len(res)>0:
        buttons.append(res)
    buttons.append([InlineKeyboardButton('Ortga', callback_data='back')])
    return InlineKeyboardMarkup(buttons)


def course_register_main_button(course_id):
    buttons = [
        [InlineKeyboardButton('Kursga yozilish', callback_data=f"{course_id}")],
        [InlineKeyboardButton("Ortga", callback_data='back')]
    ]
    return InlineKeyboardMarkup(buttons)


def phone_button():
    button = [
        [KeyboardButton('Raqam yuborish', request_contact=True)]
    ]
    return ReplyKeyboardMarkup(button, resize_keyboard=True)


def admin_main_button():
    button = [
        ['Kurs qo\'shish'],
        ["O'qituvchi qo'shish"]
    ]

    return ReplyKeyboardMarkup(button, resize_keyboard=True)