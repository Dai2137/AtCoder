from atcoder.dsu import DSU
N, M = map(int, input().split())
uf = DSU(N)
G = [[] for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    u-=1
    v-=1
    G[u].append(v)
    G[v].append(u)
    uf.merge(u, v)

print(M - N + len(uf.groups()))



# visited = [None] * N
# cnt = 0
# def dfs(u):
#     visited[u] = True
#     for v in G[u]:
#         if not visited[v]:
#             dfs(v)


    
