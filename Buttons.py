from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
bizningkurslar = 'Bizning Kurslar'
bizning_ustozlar = 'Bizning Ustozlar'
biz_haqimizda = 'Biz haqimizda'
def main_button():
        button = [
            [bizningkurslar],
            [bizning_ustozlar, biz_haqimizda]
        ]

        return ReplyKeyboardMarkup(button, resize_keyboard=True)

