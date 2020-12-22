import re

# s = ' долг: '
f = open('10_demo2021.txt')
s = f.read().lower()
f.close()

lst = re.findall(r'\bдолг\b',s)

print(lst)