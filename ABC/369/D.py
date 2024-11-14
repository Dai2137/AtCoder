N=int(input())
A=list(map(int,input().split()))
INF=10**9+100
dp = [[-INF]*2 for _ in range(N+1)]

dp[0][0] = 0
dp[0][1] = -INF

for i in range(N):
  dp[i+1][0] = max(dp[i+1][0], dp[i][0], dp[i][1]+(2*A[i]))
  dp[i+1][1] = max(dp[i+1][1], dp[i][1], dp[i][0]+A[i])

print(max(dp[N][0],dp[N][1]))
