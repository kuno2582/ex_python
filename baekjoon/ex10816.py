n = int(input())
r1 = list(map(int, input().split()))
m = int(input())
r2 = list(map(int, input().split()))
jsonArr = {}

for i in sorted(r1):
    str_i = str(i)
    if str_i in jsonArr:
        jsonArr[str_i] += 1
    else:
        jsonArr[str_i] = 1
for j in r2:
    str_j = str(j)
    if str_j in jsonArr:
        print(jsonArr[str_j], end=' ')
    else:
        print(0, end=' ')
