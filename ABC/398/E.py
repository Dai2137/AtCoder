N = int(input())

G = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

col = [0] * N

def dfs(x, p):
    for u in G[x]:
        if u == p:
            continue
        col[u] = 1 ^ col[x]
        dfs(u, x)

dfs(0, -1)

rest = set()

for i in range(N):
    if col[i]: continue
    for j in range(N):
        if not col[j]: continue
        if j not in G[i]:
            rest.add((min(i, j), max(i, j)))

L = len(rest)
if L % 2:
    print("First")
else:
    print("Second")

while True:
    if L % 2:
        i, j = rest.pop()
        print(i + 1, j + 1)
    else:
        i, j = map(int, input().split())
        if i == -1:
            exit()
        i -= 1
        j -= 1
        rest.remove((i, j))
    
    L -= 1
    