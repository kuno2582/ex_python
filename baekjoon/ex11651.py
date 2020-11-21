import sys
n, r = int(sys.stdin.readline()), [0]*200001
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    t = 100000 + y
    if r[t] == 0:
        r[t] = [x]
    else:
        r[t].append(x)
        r[t].sort()

for i, j in enumerate(r):
    if j != 0:
        for k in range(len(j)):
            print(j[k], i-100000)
