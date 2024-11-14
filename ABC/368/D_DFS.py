import pypyjit
import sys

pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10**9)

N, K = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    g[A - 1].append(B - 1)
    g[B - 1].append(A - 1)
V = list(map(int, input().split()))
a = [0] * N
for v in V:
    a[v - 1] = 1


def dfs(u, p):
    c, ans = a[u], 0
    ok = True
    for v in g[u]:
        if v != p:
            c_sub, ans_sub = dfs(v, u)
            c += c_sub
            ans += ans_sub
            ok &= c_sub < K
    ans += ok and (c > 0)
    return c, ans


print(dfs(0, -1)[1])
