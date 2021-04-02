'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3776
В файле записана последовательность натуральных чисел. 
Из этой последовательности нужно выбрать четыре числа, 
чтобы их сумма делилась на 9 и была наименьшей. 
Какую наименьшую сумму можно при этом получить?
Каждая из N строк содержит одно натуральное число, не превышающее 10**8.
'''
f = open('27-57c.txt')
lines = f.readlines()
f.close()

n = int(lines[0])
lst = sorted(map(int, lines[1:n+1]))[:150]
n = len(lst)
# print(lst)
sm = 4*10**8
for p1 in range(n-4):
    for p2 in range(p1+1,n-3):
        for p3 in range(p2+1,n-2):
            for p4 in range(p3+1,n-1):
                st = lst[p1]+lst[p2]+lst[p3]+lst[p4]
                if sm > st and st % 9 == 0:
                    sm = st
print(sm)
# 406773 для файла Б
