import sys
n, c = map(int, sys.stdin.readline().split())
int_r = []
for _ in range(n):
    int_r.append(int(sys.stdin.readline()))
int_r.sort()
s, e = 1, int_r[-1] - int_r[0]
while s <= e:
    mid = (s+e) // 2
    cnt = 1
    o = int_r[0]
    for i in range(n):
        if mid <= int_r[i] - o:
            cnt += 1
            o = int_r[i]

    if cnt >= c:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1
print(ans)
