from itertools import *
n, m = map(int, input().split())
r = [i for i in combinations([x for x in range(1, n+1)], m)]
for j in r:
    print(' '.join(map(str, j)))