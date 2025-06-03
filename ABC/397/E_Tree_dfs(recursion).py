import sys
sys.setrecursionlimit(10**9)

N, K = map(int, input().split())

NK = N * K
T = [[] for _ in range(NK)]

for _ in range(NK - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    T[u].append(v)
    T[v].append(u)

ok = True

def dfs(v: int, p: int = -1) -> int:
    global ok
    res = 1
    deg = 0
    for u in T[v]:
        if u != p:
            sz = dfs(u, v)
            res += sz
            if sz % K != 0:
                deg += 1

    if res % K != 0:
        deg += 1
    
    if deg > 2:
        ok = False

    return res

dfs(0)

print("Yes" if ok else "No")
