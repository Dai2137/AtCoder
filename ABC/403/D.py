N, D = map(int, input().split())
A = list(map(int, input().split()))

if D == 0:
    print(N - len(set(A)))
    exit()
else:
    M = 10 ** 6 + 1
    cnt = [0] * (M + 1)
    for i in range(N):
        cnt[A[i]] += 1
    ans = 0
    
    INF = 10**20 + 7
    dp = [INF] * (M + 1)
    
    for i in range(D):
        dp[i] = 0
        if i + D < M + 1:
            dp[i + D] = min(cnt[i], cnt[i + D])
        if i + 2 * D < M + 1:
            for j in range(i + 2 * D, M + 1, D):
                dp[j] = min(dp[j - D] + cnt[j], dp[j - 2 * D] + cnt[j - D])
    for i in range(M, M - D, -1):
        ans += dp[i]
print(ans)