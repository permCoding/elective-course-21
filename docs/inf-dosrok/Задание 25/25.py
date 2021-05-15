'''
Пусть M – сумма минимального и максимального натуральных делителей
целого числа, не считая единицы и самого числа. Если таких делителей
у числа нет, то считаем значение M равным нулю.
Напишите программу, которая перебирает целые числа, большие 452 021,
в порядке возрастания и ищет среди них такие, для которых значение M
при делении на 7 даёт в остатке 3. Вывести первые 5 найденных чисел
и соответствующие им значения M.
Формат вывода: для каждого из 5 таких найденных чисел в отдельной строке
сначала выводится само число, затем – значение М.
Строки выводятся в порядке возрастания найденных чисел.
Например, для числа 20 М = 2 + 10 = 12.
452025 150678
452029 23810
452034 226019
452048 226026
452062 226033
'''

def get(n):
    mn, mx = 0, 0
    for j in range(2, n):
        if n%j==0:
            mn = j
            mx = n//j
            break
    return mn + mx

i = 452021
cnt = 0
while True:
    i += 1
    m = get(i)
    if m%7==3:
        print(i, m)
        cnt += 1
    if cnt > 4:
        break
    