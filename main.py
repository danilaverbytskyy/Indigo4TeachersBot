import telebot
from config import Config
from bot.core.database import init_db
from bot.handlers.common import register_common_handlers
import threading
import requests
import time
from flask import Flask

# Создаем Flask приложение для веб-сервера
app = Flask(__name__)


@app.route('/')
def home():
    """Простая страница для проверки работы сервера"""
    return "🤖 Telegram Bot is running! ✅"


def run_web_server():
    """Запускает веб-сервер в отдельном потоке"""
    app.run(host='0.0.0.0', port=8080)


def self_ping():
    """Регулярно пингует приложение, чтобы предотвратить сон"""
    while True:
        try:
            # Получаем URL проекта из переменных окружения Replit
            project_name = os.environ.get('REPL_SLUG')
            user_name = os.environ.get('REPL_OWNER')

            if project_name and user_name:
                url = f"https://{project_name}.{user_name}.repl.co"
                requests.get(url, timeout=10)
                print(f"Self-ping sent to {url}")
            else:
                print("Could not determine Replit URL for self-ping")

        except Exception as e:
            print(f"Self-ping error: {e}")

        # Интервал 4 минуты (меньше чем 5-минутный таймаут сна Replit)
        time.sleep(240)


def main():
    # Инициализация
    config = Config()
    bot = telebot.TeleBot(config.BOT_TOKEN)

    # База данных
    init_db()

    # Регистрация обработчиков
    register_common_handlers(bot, config)
    # ... другие обработчики

    # Запускаем веб-сервер в фоновом режиме
    web_thread = threading.Thread(target=run_web_server, daemon=True)
    web_thread.start()
    print("Web server started on port 8080")

    # Запускаем self-ping в фоновом режиме
    ping_thread = threading.Thread(target=self_ping, daemon=True)
    ping_thread.start()
    print("Self-ping service started")

    print('Bot is successfully running ✅')

    # Запуск бота
    bot.infinity_polling()


if __name__ == "__main__":
    # Для корректной работы в Replit
    import os

    os.environ['FLASK_ENV'] = 'development'

    main()