from itertools import *
n, m = map(int, input().split())
r = [i for i in permutations([i for i in range(1, n+1)], m)]
for k in r:
    print(' '.join(map(str, k)))
