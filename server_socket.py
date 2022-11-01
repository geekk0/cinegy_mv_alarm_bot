import socket
# import pyautogui
import threading
import datetime

from bot import send_alarm


"""def set_alert(msg):
    pyautogui.alert(text=msg, title="Logger status")"""


def stream_fail():

    send_alarm()

    """if "event channel" in msg:
        channel = msg.split("event")[1].split()[1][:-1]
        print(channel)
        text = "channel " + channel + " is bad"
        # pyautogui.alert(text=text, title="Channel alarm!")"""


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.bind(('', 5500))  # связываем сокет с портом, где он будет ожидать сообщения
sock.listen(10)  # указываем сколько может сокет принимать соединений
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()  # начинаем принимать соединения
    print('connected:', addr)  # выводим информацию о подключении
    print(datetime.datetime.now())
    data = conn.recv(1024)  # принимаем данные от клиента, по 1024 байт
    data_string = data.decode("utf-8")
    # print(data_string)

    alert_thread = threading.Thread(target=stream_fail, daemon=True)
    alert_thread.start()


# conn.send(data.upper())  # в ответ клиенту отправляем сообщение в верхнем регистре
# conn.close()  # закрываем соединение



