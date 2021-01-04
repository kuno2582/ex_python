import sys
k, n = map(int, input().split())
int_r = []
for i in range(k):
    int_r.append(int(sys.stdin.readline()))
#
# k, n = 4, 11
# str_r = """802
# 743
# 457
# 539"""
# int_r = list(map(int, str_r.split('\n')))
h, l = sum(int_r)//n, 1
while l <= h:
    mid = (h+l) // 2
    cnt = sum([x//mid for x in int_r])
    if cnt < n:
        h = mid - 1
    elif cnt >= n:
        l = mid + 1
        ans = mid
print(ans)
