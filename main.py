import telebot
from config import Config
from bot.core.database import init_db
from bot.handlers.common import register_common_handlers
import threading
import requests
import time
import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "🤖 Telegram Bot is running! ✅"


@app.route('/ping')
def ping():
    return "Pong!"


def run_web_server():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    """Двойная защита от сна: UptimeRobot + внутренний пинг"""
    while True:
        try:
            # 1. Пинг через UptimeRobot
            public_url = f"https://{os.environ.get('REPL_SLUG')}.{os.environ.get('REPL_OWNER')}.repl.co"
            requests.get(public_url, timeout=5)

            # 2. Внутренний пинг (не требует DNS)
            requests.get("http://localhost:8080/ping", timeout=5)

            print("Keep-alive ping successful")
        except Exception as e:
            print(f"Keep-alive error: {e}")

        # Пингуем каждые 3 минуты (меньше интервал сна Replit)
        time.sleep(180)


def main():
    # Инициализация
    config = Config()
    bot = telebot.TeleBot(config.BOT_TOKEN)

    # База данных
    init_db()

    # Регистрация обработчиков
    register_common_handlers(bot, config)
    # ... другие обработчики

    # # Запускаем веб-сервер
    # web_thread = threading.Thread(target=run_web_server, daemon=True)
    # web_thread.start()
    # print("Web server started on port 8080")
    #
    # # Даем время серверу запуститься
    # time.sleep(2)
    #
    # # Запускаем систему поддержания активности
    # keep_alive_thread = threading.Thread(target=keep_alive, daemon=True)
    # keep_alive_thread.start()
    # print("Keep-alive service started")

    print('Bot is successfully running ✅')
    bot.infinity_polling()


if __name__ == "__main__":
    # Для стабильной работы в Replit
    os.environ['FLASK_ENV'] = 'production'

    main()