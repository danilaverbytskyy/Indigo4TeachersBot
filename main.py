#!/home/danilamolotov/.virtualenvs/myvirtualenv/bin/python

import telebot
from config import Config
from bot.core.database import init_db
from bot.handlers.common import register_common_handlers

def main():
    config = Config()
    bot = telebot.TeleBot(config.BOT_TOKEN)

    init_db()

    register_common_handlers(bot, config)

    print('Bot is successfully running ✅')
    bot.infinity_polling()


if __name__ == "__main__":
    main()