import sys

n, r = int(sys.stdin.readline()), []
for i in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        r.pop()
    else:
        r.append(k)
print(sum(r))