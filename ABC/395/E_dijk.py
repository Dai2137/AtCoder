import heapq
N, M, X = map(int, input().split())

INF = 10**20

G = [[] for _ in range(2 * N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[2 * u].append(2 * v)
    G[2 * v + 1].append(2 * u + 1)


dist = [INF] * (2 * N)

# (d:その時点の頂点vへの最短距離, v)
pq = [(0, 0)]

dist[0] = 0

def push(v, d):
    if d >= dist[v]:
        return
    dist[v] = d
    heapq.heappush(pq, (d, v))


while pq:
    d, v = heapq.heappop(pq)
    if dist[v] != d:
        continue
    for u in G[v]:
        push(u, d + 1)
    push(v ^ 1, d + X)

print(min(dist[2 * (N - 1)], dist[2 * (N - 1) + 1]))