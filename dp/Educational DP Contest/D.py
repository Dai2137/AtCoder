N,W = map(int,input().split())
w,v=[],[]
INF=10**10

for i in range(N):
  wi,vi=map(int,input().split())
  w.append(wi)
  v.append(vi)

dp=[[-INF]*(W+1) for _ in range(N+1)]

for i in range(len(dp[0])):
  dp[0][i]=0

for i in range(1,N+1):
  for j in range(1,W+1):
    if j-w[i-1]>=0:
      dp[i][j] = max(dp[i][j], dp[i-1][j-w[i-1]] + v[i-1])
    dp[i][j] = max(dp[i][j], dp[i-1][j])

print(dp[N][W])