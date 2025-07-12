import os

from telebot import TeleBot
from bot.core.database import engine
from bot.core.keyboards import useful_links_keyboard, BUTTON_READY_LESSONS, BUTTON_USEFUL_LINKS, main_menu, BUTTON_BACK, \
    lesson_choices
from bot.handlers.user_handler import set_user_state, get_user_state
from bot.models.bot_user import BotUser
from sqlalchemy.orm import Session

from bot.models.useful_link import UsefulLink

STATE_MAIN_MENU = "main_menu"
STATE_USEFUL_LINKS = "useful_links"
STATE_READY_LESSONS = "ready_lessons"
STATE_ADDITIONAL_MATERIALS = "additional_materials"

def register_common_handlers(bot: TeleBot, config):
    @bot.message_handler(commands=['start'])
    def start(message):
        user_id = message.from_user.id
        firstname = message.from_user.first_name
        lastname = message.from_user.last_name
        username = message.from_user.username
        with Session(autoflush=False, bind=engine) as db:
            existing_user = db.query(BotUser).filter_by(user_id=user_id).first()

            if existing_user:
                existing_user.username=username
                existing_user.state_id=1
            else:
                bot_user = BotUser(
                    user_id=user_id,
                    firstname=firstname,
                    lastname=lastname,
                    username=username,
                )
                db.add(bot_user)

            db.commit()

        set_user_state(user_id, STATE_MAIN_MENU)

        bot.send_message(
            message.chat.id,
            f"Hi {firstname}! What are you searching for?🔠",
            reply_markup=main_menu()
        )

    @bot.callback_query_handler(func=lambda call: call.data == BUTTON_USEFUL_LINKS)
    def handle_useful_links(call):
        user_id = call.from_user.id
        set_user_state(user_id, STATE_USEFUL_LINKS)

        links_text = "🔗 Полезные ссылки:\n\n"

        with Session(autoflush=False, bind=engine) as db:
            useful_links = db.query(UsefulLink).all()
            for link in useful_links:
                links_text += f"<a href='{link.link}'>• {link.title}</a>\n"

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
        set_user_state(user_id, STATE_READY_LESSONS)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Выберите категорию уроков:",
            reply_markup=lesson_choices()
        )

    @bot.callback_query_handler(func=lambda call: call.data == BUTTON_BACK)
    def handle_back(call):
        user_id = call.from_user.id
        previous_state = get_user_state(user_id)

        if previous_state in [STATE_USEFUL_LINKS, STATE_READY_LESSONS, STATE_ADDITIONAL_MATERIALS]:
            set_user_state(user_id, STATE_MAIN_MENU)
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Вы вернулись в главное меню",
                reply_markup=main_menu()
            )
        else:
            bot.answer_callback_query(call.id, "Вы уже в главном меню")
