import os
import telebot
from config import Config
from bot.core.database import init_db
from bot.handlers.common import register_common_handlers
import threading
import requests
import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "🤖 Telegram Bot is running! ✅"


def run_web_server():
    app.run(host='0.0.0.0', port=8080)


def self_ping():
    """Регулярно пингует собственный веб-интерфейс для поддержания активности"""
    time.sleep(10)  # Даем время для запуска сервера

    while True:
        try:
            # Получаем URL проекта из переменных окружения Replit
            project_name = os.environ.get('REPL_SLUG')
            user_name = os.environ.get('REPL_OWNER')

            if project_name and user_name:
                url = f"https://{project_name}.{user_name}.repl.co"
                response = requests.get(url, timeout=10)
                print(f"Self-ping status: {response.status_code} | Sent to {url}")
            else:
                # Если переменные окружения недоступны, используем localhost
                requests.get("http://localhost:8080", timeout=5)
                print("Self-ping sent to localhost")

        except Exception as e:
            print(f"Self-ping error: {str(e)}")

        # Интервал 4 минуты (меньше чем 5-минутный таймаут сна Replit)
        time.sleep(240)


def main():
    config = Config()
    bot = telebot.TeleBot(config.BOT_TOKEN)

    # База данных
    init_db()

    # Регистрация обработчиков
    register_common_handlers(bot, config)
    # ... другие обработчики

    # Запускаем веб-сервер
    web_thread = threading.Thread(target=run_web_server, daemon=True)
    web_thread.start()
    print("Web server started on port 8080")

    # Запускаем self-ping
    ping_thread = threading.Thread(target=self_ping, daemon=True)
    ping_thread.start()
    print("Self-ping service started")

    print('Bot is successfully running ✅')
    bot.infinity_polling()


if __name__ == "__main__":
    # Для корректной работы в Replit
    os.environ['FLASK_ENV'] = 'development'
    os.environ['PORT'] = '8080'

    main()