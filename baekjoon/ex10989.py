import sys
n, d = int(input()), {}

for i in range(n):
    k = int(sys.stdin.readline())
    if k in d:
        d[k] += 1
    else:
        d[k] = 1

for k in sorted(d):
    for j in range(d.get(k)):
        print(k)
