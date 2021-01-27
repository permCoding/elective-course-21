import re
import os

os.system('cls' if os.name == 'nt' else 'clear')

line = 'XXXYYXXYZXXYZXY'
# line = 'XXXYYXXYXZXXYYZXY'
line = 'XXY'

query = r'((XYZ)*(XY|X)?)'
# query = r'(((XYZ){1,}(XY|Y)?)|(XY)|(X))'
lst = re.findall(query, line) # находит все подходящие подстроки

print(lst)

max_count = max(map(lambda item: len(item[0]), lst))
print(max_count)