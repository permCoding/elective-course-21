# задача 16 из Демо

F = [0, 1]
for n in range(2, 26+1):
    if n%2 == 0:
        F.append(n + F[n-1])
    else:
        F.append(2 * F[n-2])
print(F[26])