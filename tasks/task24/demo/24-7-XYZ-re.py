import re

f = open('24_XYZ.txt')
line = f.readline()
f.close()

query = r'((XYZ)*(XY|X)?)'
lst = re.findall(query, line) # находит все подходящие подстроки

max_count = 0 # максимальная длина подстроки
for item in lst:
	max_count = max(len(item[0]), max_count)
print(max_count)

max_count = max(map(lambda item: len(item[0]), lst))
print(max_count)