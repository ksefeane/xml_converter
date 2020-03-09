import xml.etree.ElementTree as ET
import re
import sys, os

thisFile = sys.argv[1]
out = thisFile.replace('xml', 'csv')

tree = ET.parse(thisFile)
root = tree.getroot()
i = tree.iter()
text = []
for x in i:
	text.append(x.text)

a = 0
i = 0
j = 0
end = 11
titles = []
headers = ''
data = []
info = []

if not os.path.exists('csv'):
	os.mkdir('csv')

for x in text:
	if x is None or "\n" in x:
		continue
	x = re.sub(',', ' \ ', x)
	data.append(x)

for x in data:
	if a == 0:
		if "Rules = " in x:
			a = 1
		titles.append(x)
	elif a == 1:
		if "Logon Time" in x:
			a = 2
		x = x[:-1]
		headers += x + ', '
	else:
		info.append(x)

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

with open(out, 'w') as f:
	for x in titles:
		f.write("%s\n" % x)
	f.write("\n")
	f.write("%s\n" % headers)
	for item in data:
		f.write("%s\n" % data[item])

print("success: ", out)
