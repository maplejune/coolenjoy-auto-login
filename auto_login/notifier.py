# !/usr/bin/env python
# -*- coding: utf-8 -*-

import telegram


def get_telegram_bot_info(file_path='../telegram.txt'):
    bot_info = open(file_path, 'r')
    bot_token, target_chat_id = bot_info.read().split(',', 2)
    bot_info.close()

    return bot_token, target_chat_id


def send_message(message):
    bot_token, target_chat_id = get_telegram_bot_info()

    bot = telegram.Bot(token=bot_token)
    bot.sendMessage(chat_id=target_chat_id, text=message)
