N, M = map(int, input().split())
INF = 10**18
d = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    d[a][b] = min(d[a][b], c)
    d[b][a] = min(d[b][a], c)

for i in range(N+1):
    d[i][i] = 0

K, T = map(int, input().split())
D = list(map(int, input().split()))
for i in range(K):
    d[D[i]][0] = T
    d[0][D[i]] = 0

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y, t = query[1], query[2], query[3]
        for i in range(N+1):
            for j in range(N+1):
                d[i][j] = min(d[i][j], d[i][x] + d[y][j] + t, d[i][y] + d[x][j] + t)
    elif query[0] == 2:
        x = query[1]
        for i in range(N+1):
            for j in range(N+1):
                d[i][j] = min(d[i][j], d[i][x] + T + d[0][j], d[i][0] + d[x][j])
    else:
        ans = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if d[i][j] != INF:
                    ans += d[i][j]
        print(ans)
