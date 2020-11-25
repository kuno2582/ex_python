from itertools import *

n, r, z = int(input()), [], []
for i in range(n):
    r.append(list(map(int, input().split())))

t = list(combinations(range(1, n+1), int(n/2)))
t1 = t[:int(len(t)/2)]
t2 = t[:-int(len(t)/2)-1:-1]

for i in range(len(t1)):
    tp1 = sum([r[x-1][y-1] for x, y in list(permutations(t1[i], 2))])
    tp2 = sum([r[x - 1][y - 1] for x, y in list(permutations(t2[i], 2))])
    z.append(abs(tp1 - tp2))
print(min(z))