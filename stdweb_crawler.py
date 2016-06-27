# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import sys

for i in range(1, 519013):
	r = requests.get('http://stdweb2.korean.go.kr/search/View.jsp?idx=' + str(i))
	data = r.text
	soup = BeautifulSoup(data)
	try:
		answer = re.findall(r'\[([^\]]+)\]', soup.find('td', {"class" : "view_bg"}).get_text())[0].split('/')
		output_tmp = str(i) + '.' + soup.find(face='새굴림', style='font-size:13px').get_text()
		for k in answer:
			tmp = list(k)
			cnt = 0
			for j in range(len(tmp)):
				if tmp[j] == '-':
					tmp[j] = soup.find(face='새굴림', style='font-size:13px').get_text().replace('-', '').replace('^', '')[cnt]
				if tmp[j] != u'\u02d0':
					cnt = cnt + 1
			output_tmp = output_tmp + '|' + ''.join(tmp) 
	except:
		try:
			output_tmp = str(i) + '.' + soup.find(face='새굴림', style='font-size:13px').get_text() + '|' + soup.find(face='새굴림', style='font-size:13px').get_text().replace('-', '').replace('^', '')
		except:
			output_tmp = str(i) + '/' + '[empty]'
	print output_tmp.encode('utf-8')
	sys.stdout.flush()
	if i % 100 == 0:
		sys.stderr.write(str(i) + "\n")