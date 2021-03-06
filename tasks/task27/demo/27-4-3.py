f = open('27-4-C.txt')
n = int(f.readline())

result = 0
m, m2, m7 = 0, 0, 0
m14_1, m14_2 = 0, 0

for _ in range(n):
    a = int(f.readline())
    if a % 14 == 0 and a >= m14_1:
        m14_2 = m14_1; m14_1 = a
    if a % 14 != 0 and a % 7 == 0 and a > m7: m7 = a
    if a % 14 != 0 and a % 2 == 0 and a > m2: m2 = a
    if a % 14 != 0 and a > m: m = a

f.close()
result = max(m14_1*m, m14_1*m7, m14_1*m2, m7*m2, m14_1*m14_2)
print(result)

'''
Последовательность натуральных чисел характеризуется числом Х — 
наибольшим числом, кратным 14 и являющимся произведением 
двух элементов последовательности с различными номерами. 
Гарантируется, что хотя бы одно такое произведение в последовательности есть.

Даны два входных файла (файл A и файл B), каждый из которых содержит 
в первой строке количество чисел N (1 ≤ N ≤ 100000). 
В каждой из последующих N строк записано одно натуральное число, не превышающее 1000.

В результате работы данного алгоритма при вводе данных из файла A ответ — 447552, из файла B — 994000.
'''
