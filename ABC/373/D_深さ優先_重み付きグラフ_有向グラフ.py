import pypyjit
import sys

pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10**9)

N,M = map(int,input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    u,v,w = map(int,input().split())
    u,v = u-1, v-1
    G[u].append((v, w))
    G[v].append((u, -w))

INF = 10**18 + 1
x = [INF] * N

def dfs(u):
    for v,w in G[u]:
        if x[v] == INF:
            x[v] = x[u] + w
            dfs(v)

for i in range(N):
    if x[i] == INF:
        x[i] = 0
        dfs(i)

print(*x)