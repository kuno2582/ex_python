import sys
n = int(sys.stdin.readline())
c = int(sys.stdin.readline())
cnt = 0


def dfs(v):
    global cnt
    visit[v] = True
    for i in range(n+1):
        if graph[v][i] == 1 and not visit[i]:
            cnt += 1
            dfs(i)


graph = [[0]*(n+1) for _ in range(n+1)]
visit = [False] * (n+1)
for i in range(c):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
dfs(1)
print(cnt)
