n, k = map(int, input().split())
k -= 1
r, q, t = list(range(1, n+1)), [], 0
while len(r):
    t += k
    while t >= len(r):
        t -= len(r)
    q.append(str(r.pop(t)))
print("<"+", ".join(q)+">")
