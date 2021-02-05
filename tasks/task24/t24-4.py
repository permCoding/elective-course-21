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
    u0 = t[i] == 'L' and count%3 == 0
    u1 = t[i] == 'D' and count%3 == 1
    u2 = t[i] == 'R' and count%3 == 2
    u3 = t[i] == 'L' and count%3 != 0
    if u0 or u1 or u2:
        count += 1
    elif u3:
        count = 1
    else:
        count = 0
    max_len = max(count, max_len)
print(max_len)


