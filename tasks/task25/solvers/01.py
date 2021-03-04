'''
https://inf-ege.sdamgia.ru/problem?id=27852
Напишите программу, которая ищет среди целых чисел, 
принадлежащих числовому отрезку [185 311; 185 330], 
числа, имеющие ровно четыре различных натуральных делителя. 
Для каждого найденного числа запишите эти четыре делителя 
в четыре соседних столбца на экране с новой строки. 
Делители в строке должны следовать в порядке возрастания.
'''

for x in range(185311, 185330 + 1):
    k = []
    for d in range(1, x+1):
        if x % d == 0:
            k.append(d)    
    if len(k) == 4:
        print(*k)