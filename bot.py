import telebot
import ast
from config import token

bot = telebot.TeleBot(token)


def store_listeners(listeners_dict):
    f = open("listeners.py", "w")
    f.write(str(listeners_dict))
    f.close()


def recall_listeners():
    f = open("listeners.py", "r")
    listeners = ast.literal_eval(f.read())
    f.close()
    return listeners


def send_alarm():
    listeners = recall_listeners()
    for listener in listeners.keys():
        bot.send_message(listener, "Поток упал!")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Hello, bot is running.')


@bot.message_handler(commands=["send_me_alarm"])
def messages(message):
    listeners = recall_listeners()
    listeners[message.chat.id] = message.chat.first_name
    store_listeners(listeners)
    bot.send_message(message.chat.id, "отправка уведомлений включена")


@bot.message_handler(commands=["stop_send_alarm"])
def messages(message):
    listeners = recall_listeners()
    del listeners[message.chat.id]
    store_listeners(listeners)
    bot.send_message(message.chat.id, "отправка уведомлений отключена")


@bot.message_handler(commands=["listeners_list"])
def echo(message):
    listeners = recall_listeners()
    if listeners:
        bot.send_message(message.chat.id, listeners.values())
    else:
        bot.send_message(message.chat.id, "уведомления никому не отправляются")


if __name__ == '__main__':
    bot.polling(none_stop=True)





