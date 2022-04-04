from Buttons import *
from telegram import Update
from telegram.ext import CallbackContext
from Database import *

state_main = 1
state_courses = 2
state_kurs_detail = 3
state_kurs_ism = 4
state_kurs_raqam = 5
state_teacher_kurs = 6
state_admin = 7

def start(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name}\n'
                              f"Zako o'quv markazimizning botiga xush kelibsiz", reply_markup=main_button())
    if checkuser(update.effective_user.id):
        add_user(update.effective_user.first_name, update.effective_user.last_name, f"{update.effective_user.id}")
        print("bazaga saqlandi")
    if checkadmin(update.effective_user.id):
        update.message.reply_html("Admin botimizga xush kelibsiz", reply_markup=admin_main_button())

        return state_admin


    return state_main


def command_kurslar(update: Update, context: CallbackContext):
    data = get_course_name()
    update.message.reply_text("Bizning kurslar", reply_markup=ReplyKeyboardRemove())
    update.message.reply_photo(open('images/bizning_kurslar.jpg', 'rb'), caption='Zamonaviy kurslardan birini tanlang',
                               reply_markup=course_buttons(data))
    return state_courses


def command_courses(update: Update, context:CallbackContext):
    query = update.callback_query
    data = query.data
    query.message.delete()
    if data=='back':
        query.message.reply_text("Main menu", reply_markup=main_button())
        return state_main
    else:
        course_id = int(data)
        data = get_course_detail(course_id)
        print(data)
        caption = f"""
     <b>{data[1]}</b>
• Kurs davomiyligi {data[3]} oy
• Amaliyot +{data[4]} oy
• Haftada {data[5]} kun {data[6]} soatdan
• Real proyektlar
• Darslar zapis qilib olinadi va guruhga tashlanadi
• Ishga joylashishda maslahat va yo'llanmalar


👨‍💻Kurs davomida: {data[7]} kabi texnologiyalar o'rgatiladi
Kurs narxi: {data[2]} so'm
Qo'shimcha: 
        """
        query.message.reply_photo(open('images/kurs.png', 'rb'), caption=caption, parse_mode="HTML", reply_markup=course_register_main_button(data[0]))
        return state_kurs_detail

def command_kurs_detail(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    query.message.delete()

    if data == 'back':
        data = get_course_name()
        query.message.reply_photo(open('images/bizning_kurslar.png', 'rb'),
                                   caption='Zamonaviy kurslardan birini tanlang',
                                   reply_markup=course_buttons(data))
        return state_courses
    else:
        context.user_data['kurs_id'] = data
        button = [
            [f'{update.effective_user.last_name}  {update.effective_user.first_name}']
        ]
        query.message.reply_text("Kursga yozilish uchun ismingizni yuboring: ", reply_markup=ReplyKeyboardMarkup(button, resize_keyboard=True))
        return state_kurs_ism
    # -1001754418236


def command_kurs_ism(update:Update, context:CallbackContext):
    text = update.message.text
    context.user_data['ism'] = text
    update.message.reply_text("Yaxshi endi siz bilan bog'lanish uchun raqamingizni yuboring:", reply_markup=phone_button())
    return state_kurs_raqam

def command_kurs_raqam(update: Update, context: CallbackContext):
    phone = update.message.contact.phone_number
    context.user_data['phone'] = phone
    kurs_nomi = get_course_detail(int(context.user_data['kurs_id']))[1]
    xabar = f"Ismi: {context.user_data['ism']}\n" \
            f"Raqami {phone}\n" \
            f"Qatnashmoqchi bo'lgan kursi: {kurs_nomi} "
    update.message.reply_text("Siz bilan bog'lanamiz", reply_markup=main_button())
    context.bot.send_message(chat_id = '-1001754418236', text=xabar)
    return state_main
def command_kurs_raqam_text(update: Update, context: CallbackContext):
    raqam = update.message.text
    if raqam[0]=='+':
        if raqam[1:].isdigit() and len(raqam)==13 and raqam[1:4] == '998':
            update.message.reply_text("Siz bilan bog'lanamiz", reply_markup=main_button())
            context.user_data['phone'] = raqam
            return state_main
        else:
            update.message.reply_html("Siz noto'gri formatda kiritdingiz: \n"
                                      "Qayta yuboting\n"
                                      "Masalan: <b>+998999999999</b>")
    else:
        if ((len(raqam)==12 and raqam[:3]=='998') or len(raqam)==9) and raqam.isdigit():
            update.message.reply_text("Siz bilan bog'lanamiz", reply_markup=main_button())
            context.user_data['phone'] = 'phone'
            return state_main
        else:
            update.message.reply_html("Siz noto'gri formatda kiritdingiz: \n"
                                      "Qayta yuboting\n"
                                      "Masalan: <b>+998999999999</b>")


def command_ustozlar(update: Update, context: CallbackContext):
    update.message.reply_text("Bizning Ustozlar", reply_markup=ReplyKeyboardRemove())
    data = get_course_name()
    update.message.reply_photo(open('images/bizning_kurslar.jpg', 'rb'), caption='Qaysi kurs bo\'yicha o\'qituvchilar haqida malumot olmoqchisiz?' ,
                               reply_markup=course_buttons(data))
    return state_teacher_kurs

def command_biz(update: Update, context: CallbackContext):
    update.message.reply_text("Biz haqimizda")


def command_teacher_kurs(update:Update, context:CallbackContext):
    query = update.callback_query
    data = query.data
    query.message.delete()
    if data == 'back':
        query.message.reply_text("Main menu", reply_markup=main_button())
        return state_main
    else:
        kurs_id = int(data)
        data = get_teachers_by_kursid(kurs_id)
        print(data)
        for i in data:
            caption = f"""
            <b>O'qituvchi</b>: {i[2]}
            <b>staji</b>: {i[4]} yil
            <b>Portfolio</b>: {i[5]} 
            """
            try:
                context.bot.send_photo(chat_id = update.effective_user.id, photo=open(i[3], 'rb'),
                                           caption=caption, parse_mode='HTML')

            except Exception as e:
                context.bot.send_message(chat_id=update.effective_user.id, text=caption, parse_mode='HTML')
        query.message.reply_text("Main menu", reply_markup=main_button())
        return state_main


def command_add_kurs(update:Update, context: CallbackContext):
    update.message.reply_text("Kurs nomini kiriting: ", reply_markup=ReplyKeyboardRemove())
    return 'state_kurs_name'

def command_kurs_name(update: Update, context:CallbackContext):
    text = update.message.text
    context.user_data['kurs_nomi'] = text
    update.message.reply_text("Kurs_narxini kiriting: ")
    return 'state_kurs_narxi'
def command_kurs_narxi(update: Update, context:CallbackContext):
    text = update.message.text
    if text.isdigit():
        context.user_data['kurs_narxi'] = text
        update.message.reply_text("Kurs davomiyligini raqamlarda kiriting(oy):")
        return 'state_kurs_duration'
    else:
        update.message.reply_text("Kurs narxini  qayta kiriting: \n"
                                  "Masalan: 700000")
        return 'state_kurs_narxi'
def command_kurs_duration(update: Update, context:CallbackContext):
    text = update.message.text
    if text.isdigit():
        context.user_data['kurs_duration'] = text
        update.message.reply_text("Kurs amaliyot muddatini raqamlarda kiriting(oy): ")
        return 'state_kurs_amaliyot'
    else:
        update.message.reply_html("Kurs davomiyligini  qayta kiriting: \n"
                                  "Masalan: <b>7</b> oy ")
        return 'state_kurs_duration'
def command_kurs_amaliyot(update: Update, context:CallbackContext):
    text = update.message.text
    if text.isdigit():
        context.user_data['kurs_amaliyot'] = text
        update.message.reply_text("O'rgatiladigan texnalogiyalarni vargul bilan ajratgan holatda "
                                  "qayta kiriting")
        return 'state_kurs_technology'
    else:
        update.message.reply_html("Kurs amaliyot muddatini qayta kiriting: \n"
                                  "Masalan: <b>2</b> oy ")
        return 'state_kurs_amaliyot'

def command_kurs_technology(update: Update, context:CallbackContext):
    technology = update.message.text
    context.user_data['technalogy'] = technology
    update.message.reply_html("Agar kurs haftada 3 kun 2 soatdan o'tilsa <b>Next</b>"
                              "tugmasini bosing.\n"
                              "Aks holda vergul bn ajratgan holda yuboring: (3,1.5)", reply_markup=ReplyKeyboardMarkup([['Next']], resize_keyboard=True))
    return "state_kurs_time"

def command_kurs_time(update: Update, context:CallbackContext):
    text = update.message.text
    if text == 'Next':
        update.message.reply_html("Kurs muaffaqiyatli saqlandi", reply_markup=admin_main_button())
        hafta =3
        soat = 2
    else:
        data = text.split(',')
        try:
            hafta = int(data[0])
            soat = float(data[1])
            update.message.reply_html("Kurs muaffaqiyatli saqlandi", reply_markup=admin_main_button())
        except Exception as e:
            update.message.reply_text("Siz xato kiritdingiz iltimos qayta harakat qilib ko'ring")
            return 'state_kurs_time'
    nomi =context.user_data['kurs_nomi']
    narxi =int(context.user_data['kurs_narxi'])
    davomiyligi =int(context.user_data['kurs_duration'])
    amaliyot = int(context.user_data['kurs_amaliyot'])
    technology = context.user_data['technalogy']
    add_course(nomi, narxi, davomiyligi, amaliyot, hafta, soat, technology)
    return state_admin
def command_add_teacher(update:Update, context: CallbackContext):
    pass