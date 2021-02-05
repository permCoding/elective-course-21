'''
https://inf-ege.sdamgia.ru/problem?id=27699  
Текстовый файл состоит не более чем из 10^6 символов L, D и R. 
Определите максимальную длину цепочки вида LDRLDRLDR... 
(составленной из фрагментов LDR, последний фрагмент может быть неполным).
Для выполнения этого задания следует написать программу. 
Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
19.40
'''

f = open('z24.txt')
t = f.readline()
f.close()

# t = 'LDRLDRLDRL'
# t = 'LDLDR'
max_len = 0
count = 0
for i in range(len(t)):
    if t[i] == 'L' and count%3 == 0:
        count += 1
    elif t[i] == 'D' and count%3 == 1:
        count += 1
    elif t[i] == 'R' and count%3 == 2:
        count += 1
    elif t[i] == 'L' and count%3 != 0:
        count = 1
    else:
        count = 0
    if count > max_len:
        max_len = count
print(max_len)


