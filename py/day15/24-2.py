f = open('24.txt')
s = f.readline()
f.close()

# s = 'XXXZZYYYZZXZXZXZZY'
w = 'XZZY'

cnt, max_cnt = 0, 0
i = 0
while i < len(s)-3:
    if w !=  s[i:i+4]:
        cnt += 1
        i += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 0
        i += 4

print(max_cnt)
