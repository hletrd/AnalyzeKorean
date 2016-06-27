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
		if len(j) > 1 and j[1] != u'ː':
			if re.match(u'[가-깋다-딯바-빟사-싷자-짛]', j[1]):
				original = original + '|' + j[1]
				result = True
	if result == True:
		print original.encode('utf-8')