import sys
n = int(sys.stdin.readline())
r = list(map(int, sys.stdin.readline().split()))
i, j = min(r), max(r)
print(i * j)
