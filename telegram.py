# -*- coding: utf-8 -*-
import telebot
from telebot import types
import re
#import configparser for take logins and passwords
#docs: https://www.notion.so/ezjikfrom/107-Python-de78724d6c2b47c1aa7dbe1ce2fe6a19
import sys;
sys.path.insert(0, 'C:\\garbage');
import datas

chatid_all = datas.send_message_telegram;

bot = telebot.TeleBot(datas.token_telegram)

#Keyboard start

def send_message(message):
	for i in chatid_all:
		message2 = message + '\nhttps://di-innova.bitrix24.ru/marketplace/app/8/'
		bot.send_message(i, message2)
		
		
#Р—Р°РїСѓСЃС‚РёС‚СЃСЏ, РµСЃР»Рё Р±СѓРґРµС‚ РѕС€РёР±РєР°
def send_mistake():
	bot.send_message(376510079, 'Ошибька')


@bot.message_handler()
def cautch_over(message):
	if message.chat.id not in chatid_all:
		bot.send_message(message.chat.id, 'Тебя нет в нашем списке')
		#chatid_all.append(message.chat.id)
		print(message.chat.id);
		print(chatid_all)
	else:
		bot.send_message(message.chat.id, 'Ты есть в нашем списке')
		print(chatid_all)
	
	#send_message('hi')

	
if __name__ == '__main__':
	try:
		bot.polling(none_stop=True);
	except:
		send_mistake();
		bot.polling(none_stop=True);
