def find_n(n, r):
    s, e = 0, len(r)-1
    while s <= e:
        mid = (s+e) // 2
        if r[mid] == n:
            return 1
        elif r[mid] < n:
            s = mid + 1
        elif r[mid] > n:
            e = mid - 1
    return 0


n = int(input())
nr1 = sorted(list(map(int, input().split())))
m = int(input())
nr2 = list(map(int, input().split()))
for j in nr2:
    print(find_n(j, nr1))
