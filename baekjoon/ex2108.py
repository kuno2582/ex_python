import math, sys

n, r, k = int(sys.stdin.readline()), [0]*8001, []
for i in range(n):
    t = int(sys.stdin.readline())
    r[t+4000] += 1
    k.append(t)
k.sort()
a = int(round(sum(k) / n, 0))
b = k[math.floor(n / 2)]
x, y, c = max(r), [], 0
for i, j in enumerate(r):
    if j == x:
        y.append((i-4000))
y.sort()
if len(y) > 1:
    c = y[1]
else:
    c = y[0]
d = max(k) - min(k)
print(a, b, c, d, sep='/n')

