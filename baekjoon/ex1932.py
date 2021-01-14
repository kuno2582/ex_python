import sys
# n = 5
# s = """7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5"""
# r = [list(map(int, x.split())) for x in s.split('\n')]

n, r = int(sys.stdin.readline()), []
for i in range(n):
    r.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, len(r)):
    t = []
    for j in range(len(r[i])):
        if j == 0:
            tmp = r[i][j] + r[i-1][j]
        elif j == (len(r[i]) - 1):
            tmp = r[i][j] + r[i-1][j-1]
        else:
            tmp = r[i][j] + max(r[i-1][j-1], r[i-1][j])
        t.append(tmp)
    r[i] = t
print(max(r[n-1]))
