N,K=map(int,input().split())
h=list(map(int,input().split()))

INF=10**9


# 配るDP
# dp[i]:iに到達するまでの最小コスト
dp=[INF]*N
dp[0]=0

for i in range(N):
  for k in range(1,K+1):
    if i+k<N:
      dp[i+k]=min(dp[i+k], dp[i]+abs(h[i]-h[i+k]))

print(dp[N-1])