# 模範解答
N=int(input())
S=input()
INF=10**9

def score(x,y):
    return 1 if (x-y)%3==1 else 0 if x==y else -INF

dp = [[-INF]*3 for _ in range(N+1)]

dp[0][0],dp[0][1],dp[0][2]=0,0,0


for i in range(N):
    y={"R":0,"P":1,"S":2}[S[i]]
    for k in range(3):
        for j in range(3):
            if k!=j:
                dp[i+1][k]=max(dp[i+1][k],dp[i][j]+score(k,y))

print(max(dp[N]))