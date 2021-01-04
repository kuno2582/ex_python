import sys
n, m = map(int, sys.stdin.readline().split())
r = list(map(int, sys.stdin.readline().split()))
low, high = 1, max(r)

while low <= high:
    mid = (low + high) // 2
    cnt = sum([x-mid for x in r if x-mid > 0])
    if cnt >= m:
        low = mid + 1
    else:
        high = mid - 1
print(high)
