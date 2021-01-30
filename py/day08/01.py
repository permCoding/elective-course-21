line = 'XYZZXYX'

count = 1
# цикл до предпоследнего символа в строке
# так как последний не с чем сравнивать
for i in range(len(line)-1):
    if line[i] != line[i+1]:
        count += 1

print(count)
