import sys
n, r = int(sys.stdin.readline()), [0]*201
for i in range(n):
    a, t = sys.stdin.readline().split()
    l = int(a)
    if r[l] == 0:
        r[l] = [t]
    else:
        r[l].append(t)

for x, y in enumerate(r):
    if y != 0:
        for i in range(len(y)):
            print(str(x) + ' ' + y[i])
