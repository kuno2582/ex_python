from itertools import *

n = int(input())

r = product([x for x in range(n)], repeat=2)
r2 = combinations(r, n)
# print(list(r))
# print(list(r2))
tmp = []
cnt = 0
for i in list(r2):
    r3 = combinations(i, 2)
    flg = True
    for j in list(r3):
        p1, p2 = j[0], j[1]
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        if (x1 == x2) or (y1 == y2) or (abs(x2 - x1) == abs(y2 - y1)):
            flg = False
            break
    if flg:
        tmp.append(i)
        cnt += 1
print(tmp)
print(cnt)
