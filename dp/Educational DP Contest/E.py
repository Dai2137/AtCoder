N,W = map(int,input().split())
w,v=[],[]
INF=10**10
vmax=10**5

for i in range(N):
  wi,vi=map(int,input().split())
  w.append(wi)
  v.append(vi)

dp=[[INF]*(vmax+1) for _ in range(N+1)]

dp[0][0]=0

for i in range(1,N+1):
  for j in range(vmax+1):
    if j-v[i-1]>=0:
      dp[i][j] = min(dp[i][j], dp[i-1][j-v[i-1]] + w[i-1])
    dp[i][j] = min(dp[i][j], dp[i-1][j])

for i,wmin in enumerate(dp[N]):
  if wmin <= W:
    ans = i

print(ans)