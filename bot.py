#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import telebot

import config



def send_welcome(message):
	text = 'Добро пожаловать!\nВас приветствует бот СПбГУ!'
	bot.send_message(message.chat.id, text)

def send_help(message):
	text = '''Помошь:
/help - для вывода этого сообещния
/about - о боте

Бот ничего не умеет.\nНо вы держитесь!'''
	bot.send_message(message.chat.id, text)

def send_about(message):
	text = 'Бот предназначен для помощи абитуриентам и студентам.\nОбратная связь: @pa_antya'
	bot.send_message(message.chat.id, text)


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
        	if m.text == '/start':
        		send_welcome(m)
        	elif m.text == '/help':
        		send_help(m)
        	elif m.text == '/about':
        		send_about(m)	
        	else:
        		text = 'Смотри что я могу!'
        		bot.reply_to(m, text)
            #bot.reply_to(m, m.text)

if __name__ == '__main__':
    bot = telebot.TeleBot(config.token)
    bot.set_update_listener(listener)
    bot.polling(none_stop=True)
    while True:
        time.sleep(200)
