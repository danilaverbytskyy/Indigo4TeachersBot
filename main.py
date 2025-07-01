import telebot
from config import Config
from bot.core.database import init_db
from bot.handlers.common import register_common_handlers


def main():
    # Инициализация
    config = Config()
    bot = telebot.TeleBot(config.BOT_TOKEN)

    # База данных
    init_db()

    # Регистрация обработчиков
    register_common_handlers(bot, config)
    # ... другие обработчики

    print('Bot is successfuly running ✅')
    # Запуск бота
    bot.infinity_polling()


if __name__ == "__main__":
    main()