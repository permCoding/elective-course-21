s = '1' * 101

while s.find('1111') > -1:
    i = s.find('1111')
    s = s[:i] + '22' + s[i+4:]
    i = s.find('222')
    if i > -1: 
        s = s[:i] + '1' + s[i+3:]

print(s)
'''
s.find('*') - ищет позицию первого вхождения подстроки '*' в строку s
метод может вернуть:
    0, 1, 2, 3, 4, ... - если нашёл
    -1 - если не нашёл
'''