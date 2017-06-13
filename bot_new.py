#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import telebot
import telebot.types as types

import cash
import botan
import config

#import configTest as config
bot = telebot.TeleBot(config.token)

# Инлайн-режим с непустым запросом
@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    #botan.track(config.botan_key, query.from_user.id, {}, 'inline запрос')
    kb = types.InlineKeyboardMarkup()
    # Добавляем колбэк-кнопку с содержимым "test"
    kb.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="test"))
    results = []
    single_msg = types.InlineQueryResultArticle(
        id="1", title="Press me",
        input_message_content=types.InputTextMessageContent(message_text="Решил проверить, что я умею?)"),
        reply_markup=kb
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results)

#Если сообщение на которое тыкнули из инлайн-режима
@bot.callback_query_handler(lambda call: call.inline_message_id)
def callback_inline(call):
    if call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")

# Если сообщение из чата с ботом
@bot.callback_query_handler(lambda call: call.message)
def callback_inline(call):
    if call.data == "s1":
        text = "начинаем ждать 1 секунду"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
        bot.send_message(call.message.chat.id,text)
        time.sleep(1)
        text = "прошла 1 секунда"
        bot.send_message(call.message.chat.id,text)
    if call.data == "s5":
        text = "начинаем ждать 5 секунд"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
        bot.send_message(call.message.chat.id,text)
        time.sleep(3)
        text = "прошлo около 5 секунд ;)"
        bot.send_message(call.message.chat.id,text)
    if call.data == "s10":
        text = "начинаем ждать 10 секунд"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
        bot.send_message(call.message.chat.id,text)
        time.sleep(2)
        text = "нее, 10 секунд - слишком долго. Не буду я столько жать"
        bot.send_message(call.message.chat.id,text)
    if call.data == "test":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
        text = 'Добро пожаловать!\nВас приветствует бот СПбГУ!\nДля абитуариентов и студентов, у нас есть специальные разделы на сайте. \nУкажите пожалйуйста свой статус:'
		    keyboardStart = telebot.types.InlineKeyboardMarkup()
		    callback_button0 = telebot.types.InlineKeyboardButton(text="Абитуриент", callback_data="abitur")
		    callback_button1 = telebot.types.InlineKeyboardButton(text="Студент", callback_data="students")
		    keyboardStart.add(callback_button0,callback_button1)
		    bot.send_message(message.chat.id, text,reply_markup=keyboardStart)
    if call.data == "event":
        text = "Вы выбрали раздел:\nМероприятия"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
        bot.send_message(call.message.chat.id, text)
    if call.data == "list":
        text = "Вы выбрали раздел:\nРасписание"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
        bot.send_message(call.message.chat.id, text)
    if call.data == "over":
        text = "Вы выбрали раздел:\nОбявления"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)            
        bot.send_message(call.message.chat.id, text)
    if call.data == "ab1":
        text = "Вы выбрали раздел:\nЧасто задаваыемые вопросы по постулению."
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
        bot.send_message(call.message.chat.id, text)
    if call.data == "ab2":
        text = "Вы выбрали раздел:\nИнформация об общежитиях."
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
        bot.send_message(call.message.chat.id, text)
    if call.data == "ab3":
        text = "Вы выбрали раздел:\nЧасто Даты поступления."
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
        bot.send_message(call.message.chat.id, text)
    if call.data == "ab4":
        text = "Вы выбрали раздел:\n.Состояние моей заявки."
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
        bot.send_message(call.message.chat.id, text)
    if call.data == "ab5":
        text = "Вы выбрали раздел:\nМоё место в очереди"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
        bot.send_message(call.message.chat.id, text)
    if call.data == "abitur":
        keyboard = telebot.types.InlineKeyboardMarkup()
        for text in cash.keyb["abitur"]:
            callback_button = telebot.types.InlineKeyboardButton(text=text, callback_data=cash.keyb["abitur"][text])
            keyboard.add(callback_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
        bot.send_message(call.message.chat.id, text='Вы Выбрали раздел Абитуриентов.', reply_markup=keyboard)
    if call.data == "students":
        keyboard = telebot.types.InlineKeyboardMarkup()
        for text in cash.keyb["students"]:
            callback_button = telebot.types.InlineKeyboardButton(text=text, callback_data=cash.keyb["students"][text])
            keyboard.add(callback_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text)
        bot.send_message(call.message.chat.id, text='Вы Выбрали раздел Студент.', reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    botan.track(config.botan_key, message.chat.id, message, '/start')
    text = 'Добро пожаловать!\nВас приветствует бот СПбГУ!\nДля абитуариентов и студентов, у нас есть специальные разделы на сайте. \nУкажите пожалйуйста свой статус:'
    keyboardStart = telebot.types.InlineKeyboardMarkup()
    callback_button0 = telebot.types.InlineKeyboardButton(text="Абитуриент", callback_data="abitur")
    callback_button1 = telebot.types.InlineKeyboardButton(text="Студент", callback_data="students")
    keyboardStart.add(callback_button0,callback_button1)
    bot.send_message(message.chat.id, text,reply_markup=keyboardStart)

@bot.message_handler(commands=['help'])
def send_help(message):
    botan.track(config.botan_key, message.chat.id, message, '/help')
    text = "Помошь:\n/help - это сообещние\n/about - о боте\n\nБот ничего не умеет.\nНо вы держитесь!"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['about'])
def send_about(message):
    botan.track(config.botan_key, message.chat.id, message, '/about')
    text = 'Бот предназначен для помощи абитуриентам и студентам.\nОбратная связь: @pa_antya'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['test'])
def send_help(message):
    botan.track(config.botan_key, message.chat.id, message, '/test')
    text = "вы запустили тест!"
    keyboardStart = telebot.types.InlineKeyboardMarkup()
    callback_button0 = telebot.types.InlineKeyboardButton(text="1 сек", callback_data="s1")
    callback_button1 = telebot.types.InlineKeyboardButton(text="5 сек", callback_data="s5")
    callback_button2 = telebot.types.InlineKeyboardButton(text="10 сек", callback_data="s10")
    keyboardStart.add(callback_button0,callback_button1,callback_button2)
    bot.send_message(message.chat.id, text, reply_markup=keyboardStart)

# Обычный режим
@bot.message_handler(content_types=["text"])
def any_msg(message):
    botan.track(config.botan_key, message.chat.id, message, 'empty_text')
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Что-то не то ты ввел.", reply_markup=keyboard)

if __name__ == '__main__':
    bot.polling(none_stop=True)

#YandexMetrica.setCustomAppVersion("1.13.2");
