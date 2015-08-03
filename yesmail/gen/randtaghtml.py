# -*- coding: utf-8 -*-
import string
import random


class FakeTag():
	spaces = [' ','']

	tag = {
	'table':['dir','align','cellpadding','cellspacing','border','width','style'],
	'td':['align','valign','width','style'],
	'tr':[],
	'tbody':[],
	}

	def style_gen(self):
		attr = {
		'align':random.choice(['center','left','right','']),
		'width': random.choice([str(random.randint(20,200))+random.choice(['px','%']),'auto','inherit','']),
		'border':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' red',
		}

		# Случайное количество атрибутов
		count_random = random.randint(0,len(attr.keys()))

		# Выбираем случайные атрибуты и рандомим их если больше одного
		attr_style = attr.keys()[:count_random]

		if len(attr_style)>0:
			random.shuffle(attr_style)

		# Формируем строку из атрибутов и их значений
		list_attr = []
		for a in attr_style:
			qoutes = random.choice(['\'','\"'])
			a = random.choice(self.spaces)+a+random.choice(self.spaces)+':'+random.choice(self.spaces)+attr[a]+random.choice(self.spaces)+';'
			list_attr.append(a)

		string_style = ' '.join(list_attr)
		return string_style


	def attr_gen(self,tagname):
		attr = {
		'dir':random.choice(['ltr','rtl','auto','']),
		'align':random.choice(['center','left','right','']),
		'valign':random.choice(['top','middle','bottom','baseline','']),
		'width': random.choice([str(random.randint(20,200))+random.choice(['px','%']),'auto','inherit','']),
		'cellpadding':str(random.randint(0,5)),
		'cellspacing':str(random.randint(0,5)),
		'border':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+'red',
		'style':self.style_gen(),
		# 'bgcolor':,

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
		table = '<'+tagname+' '+random.choice(self.spaces)+self.attr_gen(tagname)+random.choice(self.spaces)+'>'
		table += '<tbody '+random.choice(self.spaces)+'>'

		# Генерим tr 
		for tr in xrange(random.randint(1,7)):
			# td = '<'+random.choice(self.spaces)+'td'+random.choice(self.spaces)+attr_gen('td')+random.choice(self.spaces)+'>'
			table += '<tr '+random.choice(self.spaces)+'>'
			for i in xrange(random.randint(1,4)):
				td = '<td '+random.choice(self.spaces)+self.attr_gen('td')+random.choice(self.spaces)+'>'+'</'+random.choice(self.spaces)+'td'+random.choice(self.spaces)+'>'
				table += td
			table += '</'+random.choice(self.spaces)+'tr'+random.choice(self.spaces)+'>'

		table += '</'+random.choice(self.spaces)+'tbody'+random.choice(self.spaces)+'>'+'</'+random.choice(self.spaces)+tagname+random.choice(self.spaces)+'>'

		return table