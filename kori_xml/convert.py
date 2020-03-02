import xml.etree.ElementTree as ET
import re

tree = ET.parse('ab.xml')
root = tree.getroot()

i = tree.iter()

head = []
c_head = {}
data = []
c_data = {}
text = []
c_text = {}
params = {'Styles', 'Font', 'Style', 'Borders', 'Border', 'Alignment', 'NumberFormat', 'Column', 'Row', 'Table', 'Position', 'Color', 'FontName', 'Horizontal', 'Vertical', 'WrapText', 'Format', 'MergeAcross'}
find = {''}

def clean(str):
	x = re.sub('{.*?}', '', str)
	return x

for x in i:
	head.append(x.tag)
	data.append(x.attrib)
	text.append(x.text)

for x, y, z in zip(head, data, text):
	c_head[x] = clean(x)
	c_data[x] = y
	c_text[x] = z

#for x in data:
#	for y in x:
#		c_data[y] = clean(x[y])
#		cy = clean(y)
#		if cy in params:
#			continue
#		print(cy, end="")
#		print(' ->', c_data[y])
#	i += 1
#	if i > 500:
#		break


i = 0
j = 0
for h in head:
	if c_head[h] in params:
		continue
#	print(c_head[h], end="")
#	print('->', c_data[h], end="")
#	print('->', c_text[h])
#	print(h.text)
		break;

i = 0
#for x in head:
#		continue
#	print(c_head[x], end="")
#	for y in root.iter(x):
#		if y.text is not None:
#			print(' -> ', y.text)
#			j += 1
#		if j > 2:
#			break
#	i += 1
#	if i > 20:
#		break

#for x, y, z in zip(head, data, text):
#    print(x, "\n", , ",", z, ",")
#for x in head:
#	i += 1
#	print(x)
data = []
description = {}
headers = {'Alert ID', 'DBMS', 'Execution TIme', 'Session Id', 'Executing User', 'IP', 'Hostname', 'SQL', 'Accessed Objects', 'Cmd Type', 'Logon Time'}

for x in text:
	if x is None:
		continue
	
	if "\n" in x:
		continue
#	print(x)
	data.append(x)
	i += 1
	if i > 80:
		break;

i = 0
for x in data:
	
	
