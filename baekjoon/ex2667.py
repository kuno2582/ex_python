import sys


def bfs(x, y):
    global n
    if x < 0 or y < 0 or (x >= n) or (y >= n):
        return 0
    if visit[x][y] == 0:
        visit[x][y] = 1

        if r[x][y] == 1:
            return 1 + bfs(x+1, y) + bfs(x-1, y) + bfs(x, y+1) + bfs(x, y-1)
        else:
            return 0
    else:
        return 0


n, s = int(sys.stdin.readline()), []
for i in range(n):
    s.append(sys.stdin.readline().strip('\n'))
# s = """0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000"""
# r = [list(map(int, x)) for x in s.split("\n")]
# print(s)
r = [list(map(int, x)) for x in s]
visit = [[0] * n for x in range(n)]
result = []
for i in range(len(r)):
    for j in range(len(r[i])):
        cnt = bfs(i, j)
        if cnt > 0:
            result.append(cnt)
result.sort()
print(len(result))
for i in result:
    print(i)