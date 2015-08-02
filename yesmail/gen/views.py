# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect,render
import gen
import string
import random

class FakeTag():
	spaces = [' ','\t',' ','  ','   ','    ']
	attr = {
	'dir':random.choice(['ltr','rtl','auto','']),
	'align':random.choice(['center','left','right','']),
	'valign':random.choice(['top','middle','bottom','baseline','']),
	}

	tag = {
	'table':['dir','align'],
	'td':['align','valign'],
	'tr':[],
	'tbody':[],
	}

	def attr_gen(self,tagname):
		count_random = random.randint(0,len(self.tag[tagname]))

		# Выбираем случайные атрибуты и рандомим их если больше одного
		attr_tags = self.tag[tagname][:count_random]

		if len(attr_tags)>0:
			random.shuffle(attr_tags)

		# Формируем строку из атрибутов и их значений
		list_attr = []
		for a in attr_tags:
			qoutes = random.choice(['\'','\"'])
			a = random.choice(self.spaces)+a+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes+random.choice(self.spaces)+self.attr[a]+random.choice(self.spaces)+qoutes+random.choice(self.spaces)
			list_attr.append(a)

		string_attrs = ' '.join(list_attr)

		return string_attrs

	def tag_gen(self,tagname):
		table = '<'+random.choice(self.spaces)+tagname+random.choice(self.spaces)+'>'
		table += '<'+random.choice(self.spaces)+'tbody'+random.choice(self.spaces)+'>'

		for tr in range(random.randint(1,7)):
			td = '<'+random.choice(self.spaces)+'td'+random.choice(self.spaces)+self.attr_gen('td')+random.choice(self.spaces)+'>'
			table += '<'+random.choice(self.spaces)+'tr'+random.choice(self.spaces)+'>'
			table += td
			table += '</'+random.choice(self.spaces)+'tr'+random.choice(self.spaces)+'>'


		table += '</'+random.choice(self.spaces)+tagname+random.choice(self.spaces)+'>'

		return table





def body(request):
	fake = FakeTag()
	b = fake.tag_gen('table')

	
	return render_to_response('body.txt',{'rand':b})

# 1. Отобрать все теги и какие атрибуты у них есть, какие могут иметь значения.
# 2. Дальше отсортировать атрибуты, которые могут быть у всех тегов. Какие могут быть только у определенных.
# 3. Отсортировать какие теги, атрибуты с какими значениями влияют на внешний вид. Какие нет (пойдут для генерации муссорных блоков)
# 4. Сделать генерацию блока основного где есть ссылка и картинка.
# 5. Сделать генерацию фейкового блока
# 6. Сделать гератор случайных пробелов и табуляцию
# 7. Сделать герацию верхней части письма <head>
# 8. Сделать генератор замены mime случайный
# 9. Генератор для кодировки случайной
# 10. Генератор заголовков


# Насчет шаблонов
# Вот я добавил три - ну это мусор))

# Вообще в рандоме в пат. мне кажется должны быть только _ТЕГИ_

# Вот пример, как я вижу
# _TEGTOP_

# _ТЕГFAKE_ _FAKE_ _ENDТЕГFAKE_

# _ТЕГКОНТЕНТ_ _IMG1_ _ENDТЕГКОНТЕНТ_

# _ТЕГFAKE_ _FAKE_ _ENDТЕГFAKE_

# _ТЕГКОНТЕНТ_ _TEXT1_ _ENDТЕГКОНТЕНТ_

# _ТЕГFAKE_ _FAKE_ _ENDТЕГFAKE_

# _ТЕГКОНТЕНТ2_ _TITLE1_ _ENDТЕГКОНТЕНТ2_
# _ТЕГКОНТЕНТ2_ _MORE_ _ENDТЕГКОНТЕНТ2_

# _ТЕГFAKE_ _FAKE_ _ENDТЕГFAKE_
# _TEGEND_

# *
# _TEGTOP_ - боди. отсутупы,фоны шрифты и т.д
# _ТЕГКОНТЕНТ_ - tr таблицы и одна td. Различные стили и шрифты
# _ТЕГКОНТЕНТ2_ - tr таблицы и одна два td. Различные стили и шрифты
# _ТЕГFAKE_ - пустые td c разными стилям. Могут быть одна, две, три, четыре td в строки. Может генерить одну-две-три-ноль строки.
# _FAKE_ - типа комментов и т.д.

# Чтобы не заморачиваться с рандомом тегов - гляньте господин медведь сюда 

# GETRESPONSE
# dayzeram@mail.ru
# mp2171267