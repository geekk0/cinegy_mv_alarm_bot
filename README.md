# cinegy_mv_alarm_bot
[switch to Rus](README.RUS.md)

![python version](https://img.shields.io/badge/python-3.8.6-brightgreen)
![languages](https://img.shields.io/github/languages/top/geekk0/cinegy_mv_alarm_bot)
![last-commit](https://img.shields.io/github/last-commit/geekk0/cinegy_mv_alarm_bot)
<br>A bunch of a script that launches a server socket and a telegram bot that sends a notification. 

## Description

This program is designed to control the continuity of the broadcast automation system "Cinegy". Multiviewer module
sends a request to the port of the server on which the socket script is running, then the script, via the telegram bot sends
notification.  

## Start

1. Adding to the virtual environment: ```pip install -r reqs.txt```
2. In the config.py file add : ```token = "*bot API token*"```
3. Run on the server *server_socket.py* и *bot.py*.

## Using a bot

Use the command *"/send_me_alarm"* to add your chat_id to the notification mailing list.
<br>
*"/stop_send_alarm"*, to remove your chat_id from the notification mailing list.

## Libraries used

socket, threading, datetime, telebot, ast.