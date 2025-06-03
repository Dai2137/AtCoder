from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if v == 0:
        v = N
    G[u].append(v)
    
visited = [False] * (N + 1)
que = deque()
INF = 10 ** 20
dist = [INF] * (N + 1)
dist[0] = 0
que.append(0)

while que:
    u = que.popleft()
    visited[u] = True
    for v in G[u]:
        if visited[v]:
            continue
        if dist[v] > dist[u] + 1:
            dist[v] = dist[u] + 1
            que.append(v)

print("-1" if dist[N] == INF else dist[N])