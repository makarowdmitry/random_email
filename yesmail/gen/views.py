# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect,render
import gen
import string
import random


def body(request):
	a = ''
	attr = {
	'dir':random.choice(['ltr','rtl','auto','']),
	'align':random.choice(['center','left','right']),
	'valign':random.choice(['top','middle','bottom','baseline']),
	}

	tag = {
	'table':['dir','align'],
	'td':['align','valign'],
	}

	tag_random = random.choice(tag.keys())
	attr_random = random.randint(0,len(tag[tag_random])-1)

	tag_generate = ' '.join(['<',tag_random,tag[tag_random][attr_random]+'='+attr[tag[tag_random][attr_random]],'>'])

	# for i in range(100):
	# 	rand = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(10))
	# 	a += rand+'\n'
	# header = open('gen/templates/header.txt','r').read()

	return render_to_response('body.txt',{'rand':tag_generate})

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