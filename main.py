import telebot
from config import Config
from bot.core.database import init_db
from bot.handlers.common import register_common_handlers
import threading
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

    print('Bot is successfully running ✅')

    # Запуск бота
    bot.infinity_polling()

if __name__ == "__main__":
    # Для корректной работы в Replit
    import os

    # Установка порта из переменной окружения Replit
    os.environ['FLASK_ENV'] = 'development'
    os.environ['PORT'] = '8080'  # Явное указание порта

    main()