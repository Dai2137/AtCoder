N, X = map(int, input().split())
S = [0] * N
C = [0] * N
P = [0] * N

for i in range(N):
    S[i], C[i], P[i] = map(int, input().split())
    P[i] /= 100
dp = [[0.0] * (X + 1) for _ in range(1 << N)]

for x in range(X + 1):
    for s in range((1 << N) - 1, -1, -1):
        for i in range(N):
            xx = x - C[i]
            ss = s | (1 << i)
            if xx < 0 or s == ss:
                continue
            val = P[i] * (dp[ss][xx] + S[i]) + (1 - P[i]) * dp[s][xx]
            dp[s][x] = max(dp[s][x], val)
print(dp[0][X])