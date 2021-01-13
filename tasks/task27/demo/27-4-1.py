f = open('27-4-A.txt')
n = int(f.readline())

lst = []
for _ in range(n):
    lst.append(int(f.readline()))

f.close()

result = 0

for i in range(n):
    for j in range(n):
        if i != j:
            tmp = lst[i] * lst[j]
            if tmp > result and tmp % 14 == 0:
                result = tmp

print(result)

'''
https://inf-ege.sdamgia.ru/problem?id=27891
Последовательность натуральных чисел характеризуется числом Х — 
наибольшим числом, кратным 14 и являющимся произведением 
двух элементов последовательности с различными номерами. 
Гарантируется, что хотя бы одно такое произведение в последовательности есть.

Даны два входных файла (файл A и файл B), каждый из которых содержит 
в первой строке количество чисел N (1 ≤ N ≤ 100000). 
В каждой из последующих N строк записано одно натуральное число, не превышающее 1000.

Пример организации исходных данных во входном файле:
5
40
1000
7
28
55
Пример выходных данных для приведённого выше примера входных данных:
28000

В результате работы данного алгоритма при вводе данных из файла A ответ — 447552, из файла B — 994000.
'''
