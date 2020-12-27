from collections import deque

n = int(input())
r = deque([x+1 for x in list(range(n))])

while len(r) != 1:
    r.popleft()
    if len(r) > 1:
        t = r.popleft()
        r.append(t)

print(r[0])
