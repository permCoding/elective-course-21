line = '1 2 3 55 3 2 0 10 9'

lst = list(map(int, line.split()))

new_lst = sorted(lst)

print(lst)
print(new_lst)
