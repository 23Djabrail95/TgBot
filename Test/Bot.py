import telebot

from googletrans import Translator

translator = Translator()
bot = telebot.TeleBot('6230759452:AAEGZzEofebdMv00PS1jnFmWn2FUkBa3hzM')


# Определяем функцию для обработки сообщений
@bot.message_handler(func=lambda m: True)
def translate_message(message):
    # Определяем язык исходного текста
    src_lang = translator.detect(message.text).lang
    # Задаем целевой язык перевода
    dest_lang = 'ru' if src_lang == 'en' else 'en'

    # Переводим полученное сообщение на целевой язык
    translated_text = translator.translate(message.text, src=src_lang, dest=dest_lang).text
    # Отправляем переведенное сообщение
    bot.reply_to(message, translated_text)


# Запускаем бота
bot.polling(none_stop=True)