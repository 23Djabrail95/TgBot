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

    if message.text == '/dev':
        bot.send_message(message.chat.id, 'Разработчики:\nГадаев Салахь \nТимаев Джабраил\nБалатпиев Ибрагим')
    elif message.text == '/teacher':
        bot.send_message(message.chat.id, 'Преподователь: \n Пахаев Хусен')
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Бот может перевести введенный текст с Русского на Английский или наоборот ')
        # ПереОодим полученное сообщение на целевой язык
    translated_text = translator.translate(message.text, src=src_lang, dest=dest_lang).text

    # Отправляем переведенное сообщение
    bot.reply_to(message, translated_text)


# Запускаем бота
bot.polling(none_stop=True)