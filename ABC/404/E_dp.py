N = int(input())
C = list(map(int, input().split()))
A = list(map(int, input().split()))

C = [0] + C
A = [1] + A

def solve(C):
    n = len(C)
    dp = [10 ** 20] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        now = 10 ** 20
        for j in range(1, C[i - 1] + 1):
            if i - j >= 0:
                now = min(now, dp[i - j])
        dp[i] = min(dp[i], now + 1)

    return dp[n]
    
ans = 0
nc = []
for i in range(1, N):
    nc.append(C[i])
    if A[i]:
        ans += solve(nc)
        nc = []

print(ans)