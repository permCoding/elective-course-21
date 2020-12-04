'''
Напишите программу, которая ищет среди целых чисел, 
принадлежащих числовому отрезку [174457; 174505], 
числа, имеющие ровно два различных натуральных делителя, 
не считая единицы и самого числа. 
Для каждого найденного числа запишите эти два делителя 
в две соседних столбца на экране с новой строки 
в порядке возрастания произведения этих двух делителей. 
Делители в строке также должны следовать в порядке возрастания.
'''
a, b = 174457, 174505
for num in range(a, b + 1):
    lst = []
    for d in range(2, num):
        if num % d == 0:
            lst.append(d)
    if len(lst) == 2:
        print(*lst)