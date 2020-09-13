import vk

idForSent = '1221790'

session = (vk.AuthSession(scope='messages',app_id='', \
	user_login='', \
	user_password='',\
	access_token=''))

vkapi = vk.API(session)

vkapi.messages.send(user_id=idForSent, message=txt)


def send_message(message):
	for i in idForSent:
		txt = message + '\nhttps://realpromo.bitrix24.ru/marketplace/app/8/'
		vkapi.messages.send(user_id=idForSent, message=txt)
		
		
#Запустится, если будет ошибка
def send_mistake():
	vkapi.messages.send(user_id=idForSent, message='Я сломался! Срочно перезапусти меня')


