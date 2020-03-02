import xml.etree.ElementTree as ET
import re
import csv

tree = ET.parse('ab.xml')
root = tree.getroot()
i = tree.iter()
text = []
for x in i:
	text.append(x.text)

i = 0
j = 0
titles = []
heads = []
headers = ''
data = []
info = []

for x in text:
	if x is None or "\n" in x:
		continue
	x = re.sub(',', ' \ ', x)
	data.append(x)

a = 0
for x in data:
	if a is 0:
		if "Rules = " in x:
			a = 1
		titles.append(x)
	elif a is 1:
		if "Logon Time" in x:
			a = 2
		x = x[:-1]
		heads.append(x)
		headers += x + ', '
	else:
		info.append(x)

end = 11
headers = headers[:-2]
c = 0
i = 0
j = 0
data = {}
data[c] = ''
for x in info:
	if i == end:
		i = 0
		data[c] = data[c][:-2]
		c += 1
		data[c] = ''
	if i < end:
		data[c] += x + ', '
		i += 1

with open('result.csv', 'w') as f:
	for x in titles:
		f.write("%s\n" % x)
	f.write("\n")
	f.write("%s\n" % headers)
	for item in data:
		f.write("%s\n" % data[item])	
