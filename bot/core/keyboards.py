from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BUTTON_BACK = "◀️ Назад"
BUTTON_READY_LESSONS = "Готовые Уроки"
BUTTON_ADDITIONAL_MATERIALS = "Дополнительные материалы"
BUTTON_USEFUL_LINKS = "Полезные ссылки"
BUTTON_WARM_UPS = "Warm-ups / Ice Breakers "
BUTTON_A1_A2 = "A1 - A2"
BUTTON_B1_B2 = "B1 - B2"
BUTTON_KIDS = "Kids"
BUTTON_THEMATIC_LESSONS = "Тематические уроки"

def main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(BUTTON_READY_LESSONS,  callback_data=BUTTON_READY_LESSONS),
        InlineKeyboardButton(BUTTON_ADDITIONAL_MATERIALS, callback_data=BUTTON_ADDITIONAL_MATERIALS),
        InlineKeyboardButton(BUTTON_WARM_UPS, callback_data=BUTTON_WARM_UPS),
        InlineKeyboardButton(BUTTON_USEFUL_LINKS, callback_data=BUTTON_USEFUL_LINKS)
    )
    return markup

def useful_links_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(BUTTON_BACK, callback_data=BUTTON_BACK))
    return markup

def lesson_choices():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(BUTTON_A1_A2, url='google.com', callback_data=BUTTON_A1_A2),
        InlineKeyboardButton(BUTTON_B1_B2, callback_data=BUTTON_B1_B2),
        InlineKeyboardButton(BUTTON_KIDS, callback_data=BUTTON_KIDS),
        InlineKeyboardButton(BUTTON_THEMATIC_LESSONS, callback_data=BUTTON_THEMATIC_LESSONS),
        InlineKeyboardButton(BUTTON_BACK, callback_data=BUTTON_BACK)
    )
    return markup