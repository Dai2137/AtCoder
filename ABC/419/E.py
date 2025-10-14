N, M, L = map(int, input().split())
A = list(map(int, input().split()))

cost = [[0] * M for _ in range(L)]

for i in range(N):
    g = i % L
    for j in range(M):
        cost[g][j] += (j - A[i]) % M

dp = [[float("inf")] * M for _ in range(L)]
dp[0] = cost[0]

for i in range(L - 1):
    for j in range(M):
        for k in range(M):
            dp[i + 1][(j + k) % M] = min(dp[i + 1][(j + k) % M], dp[i][j] + cost[i + 1][k])

print(dp[L - 1][0])