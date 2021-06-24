# https://inf-ege.sdamgia.ru/problem?id=27272

k = 61
while True:
    s = '1'*k
    while s.find('111') > -1:
        s = s.replace('111','2',1)
        s = s.replace('222','11',1)
    if s == '2211':
        break
    k += 1

print(k, s)
