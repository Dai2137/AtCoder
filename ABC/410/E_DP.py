N, H, M = map(int, input().split())

dp = [[-1] * (H + 1) for _ in range(N + 1)]

for i in range(H + 1):
    dp[0][i] = M
    
for i in range(1, N + 1):
    A, B = map(int, input().split())
    for j in range(H + 1):
        if j + A < H + 1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j + A])
        dp[i][j] = max(dp[i][j], dp[i - 1][j] - B)

ans = 0
for i in range(N + 1):
    for j in range(H + 1):
        if dp[i][j] >= 0:
            ans = max(ans, i)

print(ans)


