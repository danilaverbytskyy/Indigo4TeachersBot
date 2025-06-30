from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton  # Добавлено

from bot.core.keyboards import useful_links_keyboard, BUTTON_READY_LESSONS, BUTTON_USEFUL_LINKS, main_menu, BUTTON_BACK, \
    lesson_choices

user_states = {}

STATE_MAIN_MENU = "main_menu"
STATE_USEFUL_LINKS = "useful_links"
STATE_READY_LESSONS = "ready_lessons"
STATE_ADDITIONAL_MATERIALS = "additional_materials"

def register_common_handlers(bot: TeleBot, config):
    @bot.message_handler(commands=['start'])
    def start(message):
        user_id = message.from_user.id
        user_states[user_id] = STATE_MAIN_MENU

        bot.send_message(
            message.chat.id,
            f"Hi {message.from_user.first_name}! What are you searching for?🔠",
            reply_markup=main_menu()  # Теперь возвращает inline-клавиатуру
        )

    @bot.callback_query_handler(func=lambda call: call.data == BUTTON_USEFUL_LINKS)
    def handle_useful_links(call):
        user_id = call.from_user.id
        user_states[user_id] = STATE_USEFUL_LINKS

        links_text = (
            "🔗 Полезные ссылки:\n\n"
            "<a href='https://umk-link.ru'>• УМК</a>\n"
            "<a href='https://eslbrains.com'>• ESL Brains</a>\n"
            "<a href='https://linguahouse.com'>• Lingua House</a>\n"
            "<a href='https://shadowing-technique.com'>• Shadowing</a>"
        )

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=links_text,
            parse_mode="HTML",
            reply_markup=useful_links_keyboard(),
            disable_web_page_preview=True
        )

    @bot.callback_query_handler(func=lambda call: call.data == BUTTON_READY_LESSONS)
    def handle_ready_lessons(call):
        user_id = call.from_user.id
        user_states[user_id] = STATE_READY_LESSONS

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Выберите категорию уроков:",
            reply_markup=lesson_choices()
        )

    @bot.callback_query_handler(func=lambda call: call.data == BUTTON_BACK)
    def handle_back(call):
        user_id = call.from_user.id
        previous_state = user_states.get(user_id, STATE_MAIN_MENU)

        if previous_state in [STATE_USEFUL_LINKS, STATE_READY_LESSONS, STATE_ADDITIONAL_MATERIALS]:
            user_states[user_id] = STATE_MAIN_MENU
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Вы вернулись в главное меню",
                reply_markup=main_menu()
            )
        else:
            bot.answer_callback_query(call.id, "Вы уже в главном меню")