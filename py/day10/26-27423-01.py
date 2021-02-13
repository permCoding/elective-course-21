'''
https://inf-ege.sdamgia.ru/problem?id=27423
'''

f = open('26_27423.txt')
lines = f.readlines()
f.close()

args = list(map(int, lines[0].split(' ')))

S = args[0]
N = args[1]

print(S, N)
