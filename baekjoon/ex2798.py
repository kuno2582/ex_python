# My
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
r = []

for x in range(len(arr)):
    for y in range(x + 1, len(arr)):
        for z in range(y + 1, len(arr)):
            s = arr[x] + arr[y] + arr[z]
            if s <= m:
                r.append(s)
print(max(r))

# Short
from itertools import*
b=input().split()
print(max([sum(i)for i in combinations(map(int,input().split()),3)if sum(i)<=int(b[1])]))