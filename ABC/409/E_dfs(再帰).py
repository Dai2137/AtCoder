import sys
sys.setrecursionlimit(10**6)

N = int(input())
x = list(map(int, input().split()))

T = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = input().split()
    u = int(u) - 1
    v = int(v) - 1
    w = int(w)
    T[u].append((v, w))
    T[v].append((u, w))

ans = 0

def dfs(v, p):
    global ans
    for c, w in T[v]:
        if c == p:
            continue
        dfs(c, v)
        ans += w * abs(x[c])
        x[v] += x[c]

dfs(0, -1)
print(ans)
