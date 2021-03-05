# https://inf-ege.sdamgia.ru/problem?id=15924

line = '1' * 101

while line.find('1111') > -1:

    pos = line.find('1111')
    line = line[0:pos] + '22' + line[pos+4:]

    pos = line.find('222')
    if pos > -1:
        line = line[0:pos] + '1' + line[pos+3:]

print(line)
