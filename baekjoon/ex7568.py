# My
n, r, a = int(input()), [], []
for i in range(n):
    r.append(tuple(map(int, input().split())))
for z in range(len(r)):
    x1, y1, s = r[z][0], r[z][1], 0
    for k in range(len(r)):
        x2, y2 = r[k][0], r[k][1]
        if (z != k) and (x1 < x2) and (y1 < y2):
            s += 1
    a.append(str(s+1))
print(' '.join(a))

# Short
S = [tuple(map(int, input().split())) for _ in range(int(input()))]
print(*[sum(H < h and W < w for h, w in S) + 1 for H, W in S])