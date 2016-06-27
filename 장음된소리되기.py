# -*- coding: utf-8 -*-
import re

f = open('output.txt', 'r')
lines = f.readlines()
cnt = 0
for i in lines:
	if '[empty]' in i:
		continue
	parsed = i.decode('utf-8').replace('\n', '').split('|')
	original = parsed.pop(0)
	result = False
	for j in parsed:
		if len(j) > 2 and j[1] == u'ː':
			if re.match(u'[까-낗따-띻빠-삫싸-앃짜-찧]', j[2]):
				if unichr(ord(j[2]) - 588) == original.split('.')[1].replace('-', '').replace('^', '')[1]:
					result = True
					original = original + '|' + j[2] + '|' + unichr(ord(j[2]) - 588)
	if result == True:
		print original.encode('utf-8')