# Определите количество строк, в которых 
# буква E встречается чаще, чем буква A.

f = open('inf_22_10_20_24.txt')
lines = f.readlines()
f.close()

count = 0
for line in lines
    if line.count('E') > line.count('A'):
        count += 1

print(count)
