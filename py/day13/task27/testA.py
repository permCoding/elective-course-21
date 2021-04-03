# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=3776

##f = open('27-57a.txt')
##lines = f.readlines()
##f.close()
##
##n = int(lines[0])
##print(lines)

# найти все пары, сумма которых кратна 3
lst = [1,2,3,4,5,6]
n = len(lst)
for L in range(n):
    for R in range(L+1, n):
        if (lst[L]+lst[R])%3 == 0:
            print(lst[L], lst[R])




