f = open('inf_22_10_20_18.txt')
lines = f.readlines()
f.close()

nums = map(float, lines)

m = 0 # максимальная сумма нисходящей цепочки
s = 0 # сумма чисел текущей нисходящей цепочки
pred = 0 # предыдущее число
for num in nums:
    if pred > num:
       s += num
    else:
        if s > m: m = s
        s = num
    pred = num

print(int(m))
