
import openai

from telegram import Update

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Встановлюємо API-ключі
openai.api_key = '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'
TELEGRAM_TOKEN = '8162287905:AAGUAlE2kDE-QDyD0lyRJL-EHeMDAt9kdAU'

# Функція для обробки повідомлень користувачів
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привіт! Я ваш бот. Напишіть мені щось!')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text

    try:
        # Виклик API OpenAI для отримання відповіді
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Використання нової моделі
            messages=[
                {"role": "user", "content": user_message}
            ],
            max_tokens=100
        )

        # Отримання відповіді бота
        bot_reply = response['choices'][0]['message']['content'].strip()
        await update.message.reply_text(bot_reply)

    except Exception as e:
        print(f"Помилка при обробці повідомлення: {e}")
        await update.message.reply_text("Виникла помилка при обробці вашого запиту.")

if __name__ == '__main__':
    YOUR_BOT_TOKEN = '8162287905:AAGUAlE2kDE-QDyD0lyRJL-EHeMDAt9kdAU'  # Замініть на ваш токен
    app = Application.builder().token(YOUR_BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    try:
        print("Бот запущений. Натисніть Ctrl+C для завершення.")
        app.run_polling()  # Запуск без тайм-ауту
    except KeyboardInterrupt:
        print("Бот зупинено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")







