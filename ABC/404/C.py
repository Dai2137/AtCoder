from atcoder.dsu import DSU
N, M = map(int, input().split())
uf = DSU(N)

G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
    uf.merge(a - 1, b - 1)


ans = True
for i in range(N):
    if len(G[i]) != 2:
        ans = False
        break
if len(uf.groups()) != 1:
    ans = False
print("Yes" if ans else "No")