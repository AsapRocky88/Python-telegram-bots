import re
from telegram import Update
from telegram.ext import (filters, MessageHandler, ApplicationBuilder,
                          ContextTypes, CommandHandler)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''
    Бот может здороваться на разных языках.
    Список поддерживаемых приветствий:
    - привет - русский
    - hello - английский
    - hola - испанский
    ''')

async def ru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('привет')

async def en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('hello')

async def es(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('hola')

async def not_supported(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Приветствие "{update.message.text}" не поддерживается.')

def get_greeting_filter(greeting: str):
    return filters.Regex(re.compile(f'^{greeting}$', re.IGNORECASE))

if __name__ == '__main__':

    application = ApplicationBuilder().token('YOUR_BOT_TOKEN').build()

    application.add_handler(MessageHandler(get_greeting_filter('привет'), ru))
    application.add_handler(MessageHandler(get_greeting_filter('hello'), en))
    application.add_handler(MessageHandler(get_greeting_filter('hola'), es))
    application.add_handler(MessageHandler(filters.TEXT, not_supported))

    application.run_polling()