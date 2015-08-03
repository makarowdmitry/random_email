# -*- coding: utf-8 -*-
import string
import random


class FakeTag():
	spaces = [' ','\t',' ','  ','   ','    ']

	tag = {
	'table':['dir','align'],
	'td':['align','valign','width'],
	'tr':[],
	'tbody':[],
	}

	def attr_gen(self,tagname):
		attr = {
		'dir':random.choice(['ltr','rtl','auto','']),
		'align':random.choice(['center','left','right','']),
		'valign':random.choice(['top','middle','bottom','baseline','']),
		'width': str(random.randint(20,200))+random.choice(['px']),
		}

		count_random = random.randint(0,len(self.tag[tagname]))

		# Выбираем случайные атрибуты и рандомим их если больше одного
		attr_tags = self.tag[tagname][:count_random]

		if len(attr_tags)>0:
			random.shuffle(attr_tags)

		# Формируем строку из атрибутов и их значений
		list_attr = []
		for a in attr_tags:
			qoutes = random.choice(['\'','\"'])
			a = random.choice(self.spaces)+a+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes+random.choice(self.spaces)+attr[a]+random.choice(self.spaces)+qoutes+random.choice(self.spaces)
			list_attr.append(a)

		string_attrs = ' '.join(list_attr)

		return string_attrs

	def tag_gen(self,tagname):
		table = '<'+random.choice(self.spaces)+tagname+random.choice(self.spaces)+self.attr_gen(tagname)+random.choice(self.spaces)+'>'
		table += '<'+random.choice(self.spaces)+'tbody'+random.choice(self.spaces)+'>'

		# Генерим tr 
		for tr in xrange(random.randint(1,7)):
			# td = '<'+random.choice(self.spaces)+'td'+random.choice(self.spaces)+attr_gen('td')+random.choice(self.spaces)+'>'
			table += '<'+random.choice(self.spaces)+'tr'+random.choice(self.spaces)+'>'
			for i in xrange(random.randint(1,4)):
				td = '<'+random.choice(self.spaces)+'td'+random.choice(self.spaces)+self.attr_gen('td')+random.choice(self.spaces)+'>'+'</'+random.choice(self.spaces)+'td'+random.choice(self.spaces)+'>'
				table += td
			table += '</'+random.choice(self.spaces)+'tr'+random.choice(self.spaces)+'>'

		table += '</'+random.choice(self.spaces)+'tbody'+random.choice(self.spaces)+'>'+'</'+random.choice(self.spaces)+tagname+random.choice(self.spaces)+'>'

		return table