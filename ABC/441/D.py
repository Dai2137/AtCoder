N, M, L, S, T = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, c))

ans = set()

def dfs(l, u, cost):
    global ans
    if l == L:
        if S <= cost <= T:
            ans.add(u + 1)
            return
        else:
            return
    
    for v, c in G[u]:
        dfs(l + 1, v, cost + c)

dfs(0, 0, 0)
print(*sorted(list(ans)))