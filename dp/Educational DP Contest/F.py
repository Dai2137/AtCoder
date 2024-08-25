s=input()
t=input()

dp=[[0] * (len(t)+1) for _ in range(len(s)+1)]

for i in range(len(s)):
  for j in range(len(t)):
    if s[i+1]==t[j+1]:
      dp[i+1][j+1] = dp[i][j] + 1
    else:
      dp[i+1][j+1] = max(dp[i+1][j], max[dp[i][j+1]])

ans=[]

x=len(s)
y=len(t)

while x > 0 and y > 0:
    if dp[x][y] == dp[x-1][y]: x -= 1
    elif dp[x][y] == dp[x][y-1]: y -= 1
    else: 
        x -= 1
        y -= 1
        ans += s[x]
print("".join(reversed(ans)))