# -*- coding: utf-8 -*-
import string
import random


class FakeTag():
	spaces = [' ','']
	spaces_words = [' ','   ']
	tabs = ['\n','','\n\n','\t','\t\n']
	punctuation = [',','!','?','.','.','.',',','','','-',';',':']

	tag = {
	'table':['dir','align','cellpadding','cellspacing','border','width','style','id','class'],
	'td':['align','valign','width','style','id','class'],
	'tr':[],
	'tbody':[],
	}

	def word_gen(self,count):
		words =''
		for i,ws in enumerate(range(count)):
			vowels = ['e','y','u','i','o','a']
			consonants = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

			word = ''
			for w in range(random.randint(1,2)):
				abc_list = [''.join(random.sample(vowels,random.randint(1,2))), ''.join(random.sample(consonants,random.randint(1,2)))]
				random.shuffle(abc_list)
				word += ''.join(abc_list)

			if i>0:
				words+=word+random.choice(self.spaces_words)
				if i%4==0:
					words+=random.choice(self.punctuation)
			else:
				words+=word
		return words

	def style_gen(self,opacity="no"):
		attr = {
		'align':random.choice(['center','left','right','']),
		'width': random.choice([str(random.randint(20,200))+random.choice(['px','%']),'auto','inherit','']),
		'border':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' red',
		'padding':random.choice(['inherit',str(random.randint(0,23))+random.choice(['px','%']), str(random.randint(0,23))+random.choice(['px ','% '])+str(random.randint(0,23))+random.choice(['px ','% '])+str(random.randint(0,23))+random.choice(['px ','% '])+str(random.randint(0,23))+random.choice(['px ','% '])]),
		'color':random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
		'font-family':random.choice(['Helvetica, Arial, sans-serif','Arial','Tahoma','Verdana','Helvetica']),
		'font-style':random.choice(['normal','italic','oblique','inherit']),
		'background-color':random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
		'font-size':random.choice([str(random.randint(3,18))+random.choice(['px','pt']),str(random.randint(73,216))+'%','inherit','xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']),
		'font-weight':random.choice(['bold','bolder','lighter','normal','100','200','300','400','500','600','700','800','900']),
		'height':random.choice([str(random.randint(20,200))+random.choice(['px','%']),'auto','inherit','']),
		'border-top':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' red',
		'border-bottom':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' red',
		'border-left':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' red',
		'border-right':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' red',
		'line-height':random.choice(['normal','inherit',str(random.randint(0,20))+'px',str(random.randint(0,4))+'%',str(random.randrange(0,2))]),
		'display':random.choice(['inline-block','block','none','inline','inline-table','list-item','run-in','table','table-caption','table-cell','table-column','table-row','table-row-group','table-footer-group','table-header-group','table-column-group']),
		'opacity':str(random.random()),
		}

		# Случайное количество атрибутов
		count_random = random.randint(0,round(len(attr.keys())/2))

		if opacity=="opacity":
			# Удаляем из словаря display и opacity
			attr.pop('display')
			attr.pop('opacity')
			attr_style = attr.keys()[:count_random]
			attr['display'] = 'none'
			attr['opacity'] = '0'
			attr_style+=attr_style+[random.choice(['display','opacity'])]



		else:
			attr_style = attr.keys()[:count_random]


		# Выбираем случайные атрибуты и рандомим их если больше одного
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


	def attr_gen(self,tagname,opacity="no"):
		tag_this = {
		'table':['dir','align','cellpadding','cellspacing','border','width','style','id','class'],
		'td':['align','valign','width','style','id','class'],
		'tr':[],
		'tbody':[],
		}

		attr = {
		'dir':random.choice(['ltr','rtl','auto','']),
		'align':random.choice(['center','left','right','']),
		'valign':random.choice(['top','middle','bottom','baseline','']),
		'width': random.choice([str(random.randint(20,200))+random.choice(['px','%']),'auto','inherit','']),
		'cellpadding':str(random.randint(0,5)),
		'cellspacing':str(random.randint(0,5)),
		'border':str(random.randint(0,2))+'px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' red',
		'style':self.style_gen(),
		'id':self.word_gen(1),
		'class':self.word_gen(1),
		}

		count_random = random.randint(0,len(tag_this[tagname]))

		if opacity=="opacity":
			# Удаляем из словаря style
			attr.pop('style')
			tag_this[tagname].pop(6)

			attr_tags = tag_this[tagname][:count_random]
			attr['style']=self.style_gen('opacity')	
			attr_tags += attr_tags+['style']
			
		else:
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

		qoutes = random.choice(['\'','\"'])
		string_attrs = ' '.join(list_attr+[random.choice(['data-'+self.word_gen(1)+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes+random.choice(self.spaces)+self.word_gen(1)+random.choice(self.spaces)+qoutes,'','','',''])])

		return string_attrs

	def tag_gen(self,tagname,count=1,opacity='no'):
		if opacity=='opacity':
			style_table = self.attr_gen(tagname,opacity)
		else:
			style_table = self.attr_gen(tagname)
		
		tag_str = ''
		for i in range(0,count):
			table = '<'+tagname+' '+random.choice(self.spaces)+style_table+random.choice(self.spaces)+'>'+random.choice(self.tabs)
			table += '<tbody '+random.choice(self.spaces)+'>'+random.choice(self.tabs)

			# Генерим tr 
			for tr in xrange(random.randint(1,7)):
				# td = '<'+random.choice(self.spaces)+'td'+random.choice(self.spaces)+attr_gen('td')+random.choice(self.spaces)+'>'
				table += '<tr '+random.choice(self.spaces)+'>'+random.choice(self.tabs)
				for i in xrange(random.randint(1,4)):
					td = '<td '+random.choice(self.spaces)+self.attr_gen('td')+random.choice(self.spaces)+'>'+self.word_gen(random.randint(4,17))+'</'+random.choice(self.spaces)+'td'+random.choice(self.spaces)+'>'
					table += td+random.choice(self.tabs)
				table += '</'+random.choice(self.spaces)+'tr'+random.choice(self.spaces)+'>'+random.choice(self.tabs)

			table += '</'+random.choice(self.spaces)+'tbody'+random.choice(self.spaces)+'>'+random.choice(self.tabs)+'</'+random.choice(self.spaces)+tagname+random.choice(self.spaces)+'>'+random.choice(self.tabs)
			tag_str += table

		return tag_str