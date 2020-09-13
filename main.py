# -*- coding: utf-8 -*-
import time
import random
from selenium import webdriver
import telegram;
#import configparser for take logins and passwords
#docs: https://www.notion.so/ezjikfrom/107-Python-de78724d6c2b47c1aa7dbe1ce2fe6a19
import sys;
sys.path.insert(0, 'C:\\garbage');
import datas




list_of_quest = []

def f_login(url,login,password):
	driver = webdriver.Firefox();#executable_path = 'D:\Programming\Python\bitrix24\001_parse_leads\geckodriver.exe');
	driver.get(url);
	#login
	login_field = driver.find_element_by_id("login");
	#login = driver.find_element_by_class_name("b24-network-auth-form-field-input");
	login_field.clear();
	login_field.send_keys(login);	
	

	nxt = driver.find_element_by_class_name("ui-btn.ui-btn-md.ui-btn-success.ui-btn-round.b24-network-auth-form-btn");
	#click
	nxt.click();
	nxt.click();
	#print(nxt)


	# password
	pswd = driver.find_element_by_id("password");
	pswd.send_keys(password);				
	#auth:
	nxt = driver.find_element_by_class_name("ui-btn.ui-btn-md.ui-btn-success.ui-btn-round.b24-network-auth-form-btn");
	nxt.click();	

			
	
	return driver;

def find_in_app_data(driver):
	#go in app with leads
	driver.get(datas.app_lead);
	driver.implicitly_wait(10);
	time.sleep(5);
	
	driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="app-frame"]'));
	driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="partner-application-install-select-country-iframe"]'));
	#print(driver.page_source)
	#click in search:
	while True:
		try:
			#find direction Bitrix24
			direction = driver.find_element_by_class_name('main-ui-select-name');
			direction.click();
			break;
		except:
			search = driver.find_element_by_id('b24_partner_application_filter_search');
			search.click();
	
	#find list with Bitrix24
	b24 = driver.find_elements_by_class_name('main-ui-select-inner-item-element');
	b24 = b24[1];
	b24.click();	
	
	#click find (we search leads from b24):
	
	while True:
		try:
	
			button_find = driver.find_element_by_class_name('ui-btn.ui-btn-primary.ui-btn-icon-search.main-ui-filter-field-button.main-ui-filter-find');
			driver.execute_script("arguments[0].scrollIntoView(true);", button_find);
			button_find.click();
		except:
			break;

	return driver;

def take_leads(driver):
	time.sleep(5);
	driver.get(datas.app_lead);
	driver.implicitly_wait(10);
	try:
		driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="app-frame"]'));
		driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="partner-application-install-select-country-iframe"]'));
	except:
		None;
	#take rows with leads
	all_leads_string = driver.find_elements_by_class_name('main-grid-row.main-grid-row-body');
	#print('Всего заявок:',len(all_leads_string));
	
	list_of_leads = [];
	for row in all_leads_string:
		count_column = 1;
		columns = row.find_elements_by_class_name('main-grid-cell-content');
		#print('Всего столбцов', len(columns))
		#take all data wrom lead:
		
		

		#if can't take we have 7 columns
		if len(columns) == 7:
			num_string = 1;
			#we pass taken leads:
			continue;
		#if can take we have 8 columns:
		else:
			num_string = 2;
		#take main parametres in each row
		for column in columns:
			#take description apparantly - descr is first num:
			if count_column == num_string:
				description = column.find_element_by_class_name('partner-application-b24-list-description-inner.js-description-inner');
				#print('description:',description.text)
			#take time - when we tooke lead?:
			if count_column == num_string+1:
				time_take = column.text;
				#print('time:',time_take)
			#take city:
			if count_column == num_string+2:
				city = column.text;
				#print('city:',city)
			#take can we take'Сделка в CRM' or 'ВЗЯТЬ ЗАЯВКУ':
			if count_column == num_string+4:
				can_take = column.text;
				#print(can_take);
				#print('cn we take:',can_take)
			count_column += 1;
			
		if num_string == 2:
			#search keys:
			for i in datas.keys:
				#compaire description
				if i in description.text.lower():
					#compaire city
					for i in datas.cities:
						if i in city.lower():
							#does we take?
							if 'ВЗЯТЬ ЗАЯВКУ' in can_take:
								take = row.find_element_by_class_name("partner-application-b24-list-item-submit-link.js-partner-submit-application");
								driver.execute_script("arguments[0].scrollIntoView(true);", take);	
								
								take.click();
								print('\n\n\nWe take lead\n' + city + '\n\n');
								#break;		
								#print(str(count_column) + '. ' + column.text);		

								try:
									telegram.send_message('Мы только что взяли заявку:\n' + 'Город:\n' + city + '\n----\nОписание:\n' + description.text);
								except:
									telegram.send_mistake();

if __name__ == '__main__':
		#auth 1:
	print('Тут парсим Битрикс24 и берем заявки');
	while True:
		try:
			login = datas.login[0];
			password = datas.password[0];
			driver1 = f_login(datas.portal,login,password);
			driver1 = find_in_app_data(driver1);
			
			#auth 2:
			login = datas.login[1];
			password = datas.password[1];
			driver2 = f_login(datas.portal,login,password);
			driver2 = find_in_app_data(driver2);
			
			#auth 3:
			login = datas.login[2];
			password = datas.password[2];
			driver3 = f_login(datas.portal,login,password);
			driver3 = find_in_app_data(driver3);
			break;
		except:
			driver1.quit();
			driver2.quit();
			driver3.quit();
	count0 = 1;
	count1 = 1;
	count2 = 1;
	#take new leads
	while True:
		try:
			
			rand_time = random.randrange(0,3,1);
			#count, how much we use auth for every:
				
			if rand_time == 0:
				count0 += 1;
				#we make pause evry man (one man go evry 20 sec, if they 3 (6-7 sec onone go))
				if count0 > 60:
					#take one of 2 over
					rand_time = random.randrange(1,3,1);
					if count0 == 160:
						count0 = 1;
				else:
					take_leads(driver1);
			if rand_time == 1:
				count1 += 1;
				if count1 > 160:
					rand_time = random.randrange(0,3,2);
					if count1 == 260:
						count1 = 1;
				else:
					take_leads(driver2);
			if rand_time == 2:
				count2 += 1;
				if count2 > 260:
					rand_time = random.randrange(0,2,1);
					if count2 == 360:
						count2 = 1;
				else:
					take_leads(driver3);
		except:
			#telegram.send_mistake();
			print('ошибка. наверно фильтры сбросились');
			driver1 = find_in_app_data(driver1);
			driver2 = find_in_app_data(driver2);
			driver3 = find_in_app_data(driver3);
		time.sleep(random.randrange(3,10,1));
			
		
	print('Мы че-то вылетели');
	telegram.send_mistake();
	driver.quit(); 
