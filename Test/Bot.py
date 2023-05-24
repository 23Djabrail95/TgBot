print(" ")
import telebot
from googletrans import Translator

translator = Translator()
bot = telebot.TeleBot('5970069277:AAEGlfiW4MF4F4wJgO8pr1qVx_GZczvpGoA')

# Определяем функцию для обработки сообщений
@bot.message_handler(func=lambda m: True)
def translate_message(message):
    # Определяем язык исходного текста
    src_lang = translator.detect(message.text).lang
    # Задаем целевой язык перевода
    dest_lang = 'ru' if src_lang == 'en' else 'en'
