# cinegy_mv_alarm_bot
[switch to Eng](README.md)


![python version](https://img.shields.io/badge/python-3.8.6-brightgreen)
![languages](https://img.shields.io/github/languages/top/geekk0/cinegy_mv_alarm_bot)
![last-commit](https://img.shields.io/github/last-commit/geekk0/cinegy_mv_alarm_bot)
<br>Связка из скрипта запускающего серверный сокет и телеграм-бота, отправляющего уведомление. 

## Описание

Эта программа разработана для контроля непрерывности вещания системы автоматизации "Cinegy". Модуль Multiviewer 
отправляет запрос на порт сервера, на котором запущен скрипт сокета, затем скрипт, через телеграм-бот отправляет 
уведомление.  

## Запуск

1. Добавляем в виртуальное окружение: ```pip install -r reqs.txt```
2. В файл config.py вносим : ```token = "*bot API token*"```
3. На сервере запускаем *server_socket.py* и *bot.py*.

## Использование бота

Используем команду *"/send_me_alarm"* чтобы добавить свой chat_id в список рассылки уведомлений.
<br>
*"/stop_send_alarm"*, чтобы удалить свой chat_id из списка рассылки уведомлений.

## Используемые библиотеки

socket, threading, datetime, telebot, ast.