from telebot.types import ReplyKeyboardMarkup

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Готовые Уроки")
    markup.add("Дополнительные материалы")
    markup.add("Полезные ссылки")
    return markup