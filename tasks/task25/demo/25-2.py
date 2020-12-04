a, b = 174457, 174505

for num in range(a, b + 1):
    lst = [d for d in range(2, num) if num % d == 0]
    if len(lst) == 2:
        print(*lst)
