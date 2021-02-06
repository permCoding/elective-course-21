'''
https://inf-ege.sdamgia.ru/problem?id=27854
110203; 110245
числа, имеющие ровно четыре различных
чётных натуральных делителя

1 .. 10
x
1 - 1
2 - 1, 2
3 - 1, 3
4 - 1, 2, 4
10 - 1, 2, 5, 10
'''

d = range(110203, 110245+1)

for x in d:
    count = 0
    for i in range(1, x+1):
        if i % 2 == 0 and x % i == 0:
            count += 1
    if count == 4:
        #print(x)
        for i in range(1, x+1):
            if i % 2 == 0 and x % i == 0:
                print(i)






        
        
