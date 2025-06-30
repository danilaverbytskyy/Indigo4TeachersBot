from telebot import TeleBot
from bot.core.keyboards import main_menu

def register_common_handlers(bot: TeleBot, config):
    @bot.message_handler(commands=['start'])
    def start(message):
        user = message.from_user
        bot.send_message(
            message.chat.id,
            f"Hi {user.first_name}! What are you searching for?🔠 ",
            reply_markup=main_menu()
        )