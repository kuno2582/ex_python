import sys
from operator import itemgetter

n, r = int(input()), []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    r.append((x, y))

# n = 11
# s = '''1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14'''
# r = [tuple(map(int, y.split())) for y in list(x for x in s.split('\n'))]

r.sort()
r.sort(key=itemgetter(1))
s = e = c = 0
for p in r:
    if e <= p[0]:
        s, e = p[0], p[1]
        c += 1
print(c)
