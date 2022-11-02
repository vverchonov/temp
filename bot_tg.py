import telebot
import os
from pprint import pprint

# ADD YOUR BOT TOKEN + GROUP/CHAT ID
TOKEN_ID = '5711175475:AAGlW3bhNbM9VYTeWrvB29WdhbIo1-hyDR0'
GROUP_ID = -854246374


bot = telebot.TeleBot(TOKEN_ID)
print('bot started')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    fname = message.chat.first_name
    text = ''.join(['Привет ', fname, ', \n\n1 Нажми 📎 внизу и выбери фотографии ИЛИ видео \n\n2. Нажми "отправить" \n\n**************************************************** \nБОТ НЕ ПРИНИМАЕТ ФОТО И ВИДЕО В ОДНОМ СООБЩЕНИИ \n****************************************************'])
    bot.send_message(
        message.chat.id, text)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    fname = message.chat.first_name
    text = ''.join(['', fname, ', \n\n1 Нажми 📎 внизу и выбери фотографии ИЛИ видео \n\n2. Нажми "отправить" \n\n**************************************************** \nБОТ НЕ ПРИНИМАЕТ ФОТО И ВИДЕО В ОДНОМ СООБЩЕНИИ \n****************************************************'])
    bot.send_message(
        message.chat.id, text)


@bot.message_handler(commands=['about'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, 'бот создан для благотворительной организации Просто Люди\n\nцель бота - помогать с фото/видео отчетами\nv1.0.0\n\nbot created by @vverchonov\nCopyright ©2022')


@ bot.message_handler(content_types=['photo'])
def send_text(message):
    print('GOT PHOTO')
    fname = message.chat.first_name
    text = ''.join([fname, ', cпасибо за фото!'])
    bot.reply_to(message, text)
    photo_caption = ''
    if message.caption:
        photo_caption = message.caption
    bot.send_photo(
        GROUP_ID, message.photo[-1].file_id, disable_notification=True, caption=photo_caption)


@ bot.message_handler(content_types=['video'])
def send_text(message):
    print('GOT VIDEO')
    fname = message.chat.first_name
    text = ''.join([fname, ', cпасибо за видео!'])
    bot.reply_to(message, text)
    file_info = bot.get_file(message.video.file_id)
    video_path = file_info.file_path
    print('VIDEO PATH = ', video_path)
    downloaded_file = bot.download_file(video_path)

    with open(video_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    isExist = os.path.exists(video_path)
    if isExist:
        print('VIDEO EXISTS')
        path = os.path.normcase(video_path)
        bot.send_video(GROUP_ID, video=open(
            path, 'rb'), caption=message.caption)

    os.remove(video_path)
    print('VIDEO REMOVED')


bot.infinity_polling()
