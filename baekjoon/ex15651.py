from itertools import *
n, m = map(int, input().split())
r = [i for i in product([x for x in range(1, n+1)], repeat=m)]
for j in r:
    print(' '.join(map(str, j)))
