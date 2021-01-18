from collections import deque


def dfs(v):
    visit[v] = True
    print(v, end=' ')

    for i in range(1, n+1):
        if not visit[i] and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = deque([v])
    visit[v] = False

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in range(1, n+1):
            if visit[i] and graph[v][i] == 1:
                queue.append(i)
                visit[i] = False


n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
visit = [False] * (n+1)
dfs(v)
print()
bfs(v)