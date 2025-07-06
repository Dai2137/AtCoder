from itertools import combinations

N, M = map(int, input().split())
G = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a][b] = G[b][a] = 1

all_edges = [(i, j) for i in range(N - 1) for j in range(i + 1, N)]
ans = 10 ** 18
for e in combinations(all_edges, N):
    deg = [0] * N
    for a, b in e:
        deg[a] += 1
        deg[b] += 1
    if all(d == 2 for d in deg):
        ans = min(ans, N + M - 2 * sum(G[a][b] for a, b in e))

print(ans)
