from collections import deque, defaultdict

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, W = map(int, input().split())
    graph[A].append((B, W))

visited = [set() for _ in range(N + 1)]
queue = deque()
queue.append((1, 0))  # (node, current_xor)
visited[1].add(0)

while queue:
    u, xor_val = queue.popleft()
    for v, w in graph[u]:
        new_xor = xor_val ^ w
        if new_xor not in visited[v]:
            visited[v].add(new_xor)
            queue.append((v, new_xor))

# 答えは visited[N] にある XOR 値のうちの最小値
if visited[N]:
    print(min(visited[N]))
else:
    print(-1)  # 到達不可能な場合
