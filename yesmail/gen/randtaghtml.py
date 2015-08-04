# -*- coding: utf-8 -*-
import string
import random



class Tag():
	spaces = [' ','']
	spaces_words = [' ','   ']
	tabs = ['\n','','\n\n','\t','\t\n','\n\n\n\n','\n\n\n']
	punctuation = [',','!','?','.','.','.',',','','','-',';',':']

	tag = {
	'table':['dir','align','cellpadding','cellspacing','border','width','style','id','class'],
	'td':['align','valign','width','id','class','border','style'],
	'a':['align','valign','width','id','class','border','style'],
	'img':['align','valign','width','id','class','border','style'],
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

	def style_gen(self,opacity="no",attr_effect='yes'):
		# Атрибуты и значения не влияющие на отображение
		if attr_effect=="no":
			attr = {
			'align':random.choice(['']),
			'width': random.choice(['auto','inherit','']),
			'border':'0px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' red',
			'padding':random.choice(['inherit',str(random.randint(0,3))+'px', str(random.randint(0,3))+'px'+str(random.randint(0,3))+'px'+str(random.randint(0,3))+'px'+str(random.randint(0,3))+'px']),
			'color':random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'font-family':random.choice(['Helvetica, Arial, sans-serif','Arial','Tahoma','Verdana','Helvetica']),
			'font-style':random.choice(['normal','italic','oblique','inherit']),
			'background-color': '' ,#random.choice(['#'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),'rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')']),
			'font-size':random.choice([str(random.randint(3,18))+random.choice(['px','pt']),str(random.randint(73,216))+'%','inherit','xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']),
			'font-weight':random.choice(['bold','bolder','lighter','normal','100','200','300','400','500','600','700','800','900']),
			'height':random.choice(['auto','inherit','']),
			'border-top':random.choice(['','0px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' red']),
			'border-bottom':random.choice(['','0px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' red']),
			'border-left':random.choice(['','0px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' red']),
			'border-right':random.choice(['','0px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' red']),
			'line-height':random.choice(['normal','inherit','']),
			'display':random.choice(['block','']),
			# 'opacity':str(random.random()),
			}

		else:
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
			# 'opacity':str(random.random()),
			}

		# Случайное количество атрибутов
		count_random = random.randint(0,round(len(attr.keys())/2))

		if opacity=="opacity":
			# Удаляем из словаря display и opacity
			attr.pop('display')
			# attr.pop('opacity')
			attr_style = attr.keys()[:count_random]
			attr['display'] = 'none'
			attr['opacity'] = '0'
			# attr_style+=[random.choice(['display','opacity'])]
			attr_style+=['display']+['opacity']



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


	def attr_gen(self,tagname,opacity="no",attr_effect='yes'):
		if attr_effect=="no":
			# Атрибуты и значения не влияющие на отображение
			tag_this = {
			'table':['dir','align','cellpadding','cellspacing','border','width','style','id','class'],
			'td':['align','valign','width','id','class','border','style'],
			'tr':[],
			'tbody':[],
			'a':['align','valign','width','id','class','border','style'],
			'img':['align','valign','width','id','class','border','style'],
			}

			attr = {
			'dir':random.choice(['auto','']),
			'align':random.choice(['']),
			'valign':random.choice(['']),
			'width': random.choice(['auto','inherit','']),
			'cellpadding':'0',
			'cellspacing':'0',
			'border':'0px '+random.choice(['solid','dotted','dashed','double','groove','ridge','inset','outset'])+' red',
			'style':self.style_gen(attr_effect='no'),
			'id':self.word_gen(1),
			'class':self.word_gen(1),
			}

		else:
			tag_this = {
			'table':['dir','align','cellpadding','cellspacing','border','width','style','id','class'],
			'td':['align','valign','width','id','class','border','style'],
			'tr':[],
			'tbody':[],
			'a':['align','valign','width','id','class','border','style'],
			'img':['align','valign','width','id','class','border','style'],
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
			attr_tags +=['style']

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

	def tag_fake(self,tagname,count=1,opacity='no'):
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
					td = '<td '+random.choice(self.spaces)+self.attr_gen('td')+random.choice(self.spaces)+'>'+self.word_gen(random.randint(4,17))+'</td'+random.choice(self.spaces)+'>'
					table += td+random.choice(self.tabs)
				table += '</tr'+random.choice(self.spaces)+'>'+random.choice(self.tabs)

			table += '</tbody'+random.choice(self.spaces)+'>'+random.choice(self.tabs)+'</'+tagname+random.choice(self.spaces)+'>'+random.choice(self.tabs)
			tag_str += table

		return tag_str


	def tag_general(self,tagname,count=1,opacity='no'):
		if opacity=='opacity':
			style_table = self.attr_gen(tagname,opacity)
		else:
			style_table = self.attr_gen(tagname,attr_effect='no')
		
		tag_str = ''
		for i in range(0,count):
			table = '<'+tagname+' '+random.choice(self.spaces)+style_table+random.choice(self.spaces)+'>'+random.choice(self.tabs)
			table += '<tbody '+random.choice(self.spaces)+'>'+random.choice(self.tabs)

			# Генерим tr 
			for i,tr in enumerate(xrange(random.randint(1,7))):
				# td = '<'+random.choice(self.spaces)+'td'+random.choice(self.spaces)+attr_gen('td')+random.choice(self.spaces)+'>'
				table += '<tr '+random.choice(self.spaces)+'>'+random.choice(self.tabs)

				if i == 0:
					count_td = random.randint(1,4)
					for c,m in enumerate(xrange(count_td)):
						if c == 0:
							random_for_a = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(random.randint(3,9)))
							random_for_img = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(random.randint(3,9)))
							qoutes_a = random.choice(['\'','\"'])
							qoutes_img = random.choice(['\'','\"'])
							td = '<td '+random.choice(self.spaces)+self.attr_gen('td',attr_effect='no')+random.choice(self.spaces)+'>'+'<a '+random.choice(self.spaces)+'href'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_a+'http://'+'[%%ORandText,domains_gen%%]'+'/'+random_for_a+qoutes_a+random.choice(self.spaces)+' '+self.attr_gen('a',attr_effect='no')+'>'+random.choice(self.spaces)+'<img '+random.choice(self.spaces)+'src'+random.choice(self.spaces)+'='+random.choice(self.spaces)+qoutes_img+'http://'+'[%%ORandText,domains_gen%%]'+'/'+random_for_img+'.jpg'+qoutes_img+' '+random.choice(self.spaces)+self.attr_gen('img',attr_effect='no')+'/>'+random.choice(self.spaces)+'</a'+random.choice(self.spaces)+'>'+'</td'+random.choice(self.spaces)+'>'
						else:
							td = '<td '+random.choice(self.spaces)+self.attr_gen('td','opacity')+random.choice(self.spaces)+'>'+self.word_gen(random.randint(4,17))+'</td'+random.choice(self.spaces)+'>'

						table += td+random.choice(self.tabs)
				else:
					for i in xrange(random.randint(1,3)):
						td = '<td '+random.choice(self.spaces)+self.attr_gen('td','opacity')+random.choice(self.spaces)+'>'+self.word_gen(random.randint(4,17))+'</td'+random.choice(self.spaces)+'>'
						table += td+random.choice(self.tabs)

				table += '</tr'+random.choice(self.spaces)+'>'+random.choice(self.tabs)

			table += '</tbody'+random.choice(self.spaces)+'>'+random.choice(self.tabs)+'</'+tagname+random.choice(self.spaces)+'>'+random.choice(self.tabs)
			tag_str += table

		return tag_str