'''
Текстовый файл состоит не более чем из 10^6 символов X, Y и Z. 
Определите максимальную длину цепочки вида XYZXYZXYZ... 
(составленной из фрагментов XYZ, последний фрагмент может быть неполным).
Для выполнения этого задания следует написать программу. Ниже приведён файл, 
который необходимо обработать с помощью данного алгоритма.
'''

f = open('24_XYZ.txt', 'r')
line = f.readline()
f.close()

# line = 'YZXYZXYZXYXYZXYZ'

count = 0
max_count = 0
for pos in range(len(line)):
    u1 = line[pos] == 'X' and count % 3 == 0
    u2 = line[pos] == 'Y' and count % 3 == 1
    u3 = line[pos] == 'Z' and count % 3 == 2
    if u1 or u2 or u3:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1 if line[pos] == 'X' else 0

print(max_count)