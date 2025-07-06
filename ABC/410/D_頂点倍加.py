from collections import deque
N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    A, B, W = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append((B, W))

que = deque()
que.append((0, 0))
visited = [set() for _ in range(N)]
visited[0].add(0)

while que:
    u, xor_val = que.popleft()
    for v, w in G[u]:
        new_xor = xor_val ^ w
        if new_xor not in visited[v]:
            que.append((v, new_xor))
            visited[v].add(new_xor)

if visited[N-1]:
    print(min(visited[N-1]))
else:
    print(-1)
