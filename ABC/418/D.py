N = int(input())
T = input()

dp = [[0] * 2 for _ in range(N)]

if T[0] == '0':
    dp[0][0] = 0
    dp[0][1] = 1
else:
    dp[0][0] = 1
    dp[0][1] = 0

for r in range(1, N):
    if T[r] == '0':
        dp[r][0] = dp[r - 1][1]
        dp[r][1] = dp[r - 1][0] + 1
    else:
        dp[r][0] = dp[r - 1][0] + 1
        dp[r][1] = dp[r - 1][1]

ans = 0
for i in range(N):
    ans += dp[i][0]
# print(dp)
print(ans)
