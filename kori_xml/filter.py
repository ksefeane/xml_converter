import re 

f = open('ab.xml')
tx = f.read()
f.close()

re.sub('ss:', '', tx)
re.sub(':', '', tx)

t = open("ab2.xml", "w")
t.write(tx)
t.close
