import sys

n, r = int(sys.stdin.readline()), [0] * 51
for i in range(n):
    t = sys.stdin.readline().replace('\n', '')
    l = len(t)
    if r[l] == 0:
        r[l] = [t]
    else:
        if t not in r[l]:
            r[l].append(t)
            r[l].sort()

for x, y in enumerate(r):
    if y != 0:
        for k in range(len(y)):
            print(y[k])
