import sys
N = int(input())
sys.setrecursionlimit(300100)

pos = [-1] * (N + 1)
G = [{} for _ in range(N + 1)]
vs = [[] for _ in range(N + 1)]

pos[0] = 0

tmp = 1
for i in range(1, N + 1):
    x, y = map(int, input().split())
    if y not in G[pos[x]]:
        G[pos[x]][y] = tmp
        tmp += 1
    pos[i] = G[pos[x]][y]
    vs[pos[i]].append(i)

ans = []

def dfs(v):
    global ans
    ans += vs[v]
    for u in sorted(list(G[v].keys())):
        dfs(G[v][u])

dfs(0)
print(*ans)

# import sys

# sys.setrecursionlimit(300100)

# n = int(input())
# G = [{} for i in range(n + 1)]
# vs = [[] for i in range(n + 1)]
# pos = [-1] * (n + 1) # 数列 A_i がどのノードに属しているか
# pos[0] = 0
# tmp = 1
# for i in range(1, n + 1):
#     p, y = map(int, input().split())
#     if y not in G[pos[p]]:
#         G[pos[p]][y] = tmp
#         tmp += 1
#     pos[i] = G[pos[p]][y]
#     vs[pos[i]].append(i)

# ans = []


# def dfs(i):
#     global ans
#     ans += vs[i]
#     for j in sorted(list(G[i].keys())):
#         dfs(G[i][j])


# dfs(0)
# print(*ans)
