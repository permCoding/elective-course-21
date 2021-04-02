'''23
https://inf-ege.sdamgia.ru/problem?id=33770
Найдите все натуральные числа, принадлежащие отрезку 
[106 000 000; 107 000 000]
у которых ровно три различных чётных делителя. 
В ответе перечислите найденные числа в порядке возрастания.
'''

for x in range(106000000, 107000000 + 1):
# for x in range(1, 27 + 1):    
    lst = []
    if x%2 == 0:
        for d in range(2, int(x**.5)+1):
            if x % d == 0:
                if d % 2 == 0:
                    lst.append(d)
                if (x//d)%2 == 0:
                    lst.append(x//d)
            # if d*d == x and d%2 == 0:
            #     lst.append(d)
                if len(lst) > 3:
                    break
    if len(lst) == 3:
        print(x, lst)

# это слишком медленно
