import xml.etree.ElementTree as ET
import re

tree = ET.parse('ab.xml')
root = tree.getroot()

i = tree.iter()

head = []
data = []
text = []

for x in i:
	head.append(x.tag)
	data.append(x.attrib)
	text.append(x.text)

i = 0
j = 0
titles = []
headers = []
data = []
ndata = []
description = {}

for x in text:
	if x is None or "\n" in x:
		continue
#	print(x)
	data.append(x)
	i += 1
	if i > 10:
		break;

a = 0
for x in data:
	if a is 0:
		if "Rules = " in x:
			a = 1
		titles.append(x)
	elif a is 1:
		print(x)
		if "Logon Time" in x:
			a = 2
		headers.append(x)
	else:
		ndata.append(x)
		print(x)
		

for x in ndata:
	print(x)
		
		
		
