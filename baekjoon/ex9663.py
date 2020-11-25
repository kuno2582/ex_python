# My
n = int(input())
r, d1, d2 = set(), set(), set()
cnt = 0


def dfs(n, y, r, d1, d2):
    global cnt
    if y == n:
        cnt += 1
        return

    for x in range(n):

        if (x in r) or ((x + y) in d1) or ((x - y) in d2):
            continue
        r.add(x)
        d1.add(x + y)
        d2.add(x - y)
        dfs(n, y + 1, r, d1, d2)
        r.remove(x)
        d1.remove(x + y)
        d2.remove(x - y)


dfs(n, 0, r, d1, d2)
print(cnt)


# Short
n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)


def solve(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False


solve(0)
print(ans)
