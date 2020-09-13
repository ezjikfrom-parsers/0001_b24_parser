# -*- coding: utf-8 -*-
import smtplib

gmail_user = ''
gmail_password = ''




def send_message(message): 
	message = message.encode('utf-8')
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login(gmail_user, gmail_password)
	server.sendmail(gmail_user, gmail_user, message)
	try:
		server.sendmail(gmail_user, 'p.dmitry@devellab.ru', message)
	except:
		print('РљРѕСЃС‚СЏ РІ РїСЂРѕР»РµС‚Рµ')
	try:
		server.sendmail(gmail_user, 'b.konstantin@devellab.ru', message)
	except:
		print('Р”РёРјР° РІ РїСЂРѕР»РµС‚Рµ')
	try:
		server.sendmail(gmail_user, 'n.vasiliy@devellab.ru', message)
	except:
		print('Р’Р°СЃСЏ РІ РїСЂРѕР»РµС‚Рµ')
		
	try:
		server.sendmail(gmail_user, 'a.grigoriy@devellab.ru', message)
	except:
		print('Р“СЂРёРёС€Р° РІ РїСЂРѕР»РµС‚Рµ')
		
	server.close()
	print(message)

	
#Р—Р°РїСѓСЃС‚РёС‚СЃСЏ, РµСЃР»Рё Р±СѓРґРµС‚ РѕС€РёР±РєР°
def send_mistake():
	vkapi.messages.send(user_id=idForSent, message='РЇ СЃР»РѕРјР°Р»СЃСЏ! РЎСЂРѕС‡РЅРѕ РїРµСЂРµР·Р°РїСѓСЃС‚Рё РјРµРЅСЏ')


