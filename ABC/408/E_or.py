from atcoder import dsu
N, M = map(int, input().split())

edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))
ans = 0
for i in range(29, -1, -1):
    uf = dsu.DSU(N)
    for u, v, w in edges:
       if (w >> i) | (ans >> i) == (ans >> i):
           uf.merge(u, v)
           
    if not uf.same(0, N - 1):
        ans |= (1 << i)

print(ans)
