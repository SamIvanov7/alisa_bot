import logging

import telebot

from grebne_extractor import process_files, remove_common_items

bot = telebot.TeleBot("TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
filepath = "grebni.txt"


@bot.message_handler(commands=["start"])
def send(message):
    chat_id = message.chat.id
    bot.send_message(
        chat_id,
        "Кидай 2 файла followers_1.json, и following.json. А потом пиши комманду /kill",
    )


@bot.message_handler(content_types=["document"])
def save_text(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = message.document.file_name
        with open(src, "wb") as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "Файл залетел. Есть!")
    except:
        bot.reply_to(message, "Ошибка отправления: " + str(Exception))


@bot.message_handler(content_types="text", commands=["kill"])
def send(message):
    kill_greben = process_files("followers_1.json", "following.json")

    chat_id = message.chat.id
    bot.send_message(
        chat_id,
        f"{kill_greben}. Лови файл с результатом: ",
    )

    global filepath
    bot.send_document(chat_id=message.chat.id, document=open(filepath, "rb"))


@bot.message_handler(content_types="text", commands=["send"])
def send(message):
    """Handle the /send command to send the Excel file."""
    grebni = remove_common_items
    global filepath
    bot.send_message(chat_id=message.chat.id, document=open(filepath, "rb"))


if __name__ == "__main__":
    bot.polling()
