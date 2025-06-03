T = int(input())

def solve():
    N = int(input())
    S = list(input())
    INF = 10 ** 18
    
    dp = [[INF] * 3 for _ in range(N + 1)]
    for i in range(3):
        dp[0][i] = 0
    
    for i in range(1, N + 1):
        dp[i][0] = min(dp[i][0], dp[i - 1][0] + (S[i - 1]=='1'))
        dp[i][1] = min(dp[i][1], dp[i - 1][0] + (S[i - 1]=='0'))
        dp[i][1] = min(dp[i][1], dp[i - 1][1] + (S[i - 1]=='0'))
        dp[i][2] = min(dp[i][2], dp[i - 1][1] + (S[i - 1]=='1'))
        dp[i][2] = min(dp[i][2], dp[i - 1][2] + (S[i - 1]=='1'))
        
    print(min(dp[N]))

for _ in range(T):
    solve()
