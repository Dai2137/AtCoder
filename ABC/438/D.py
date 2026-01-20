N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

INF = 10**30

dp = [[0] * N  for _ in range(3)]
dp[0][0], dp[1][0], dp[2][0] = A[0], -INF, -INF
for i in range(1, N):
    dp[0][i] = dp[0][i - 1] + A[i]
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1]) + B[i]
    dp[2][i] = max(dp[1][i - 1], dp[2][i - 1]) + C[i]

print(dp[2][N - 1])



# D, E, F, G, H = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)

# for i in range(N):
#     D[i + 1] = D[i] + A[i]
#     E[i + 1] = E[i] + B[i]
#     F[i + 1] = F[i] + C[i]

# for i in range(1, N):
#     G[i] = E[i] - F[i]
#     H[i] = D[i] - E[i]

# max_H = -10 ** 30
# for y in range(2, N):
#     max_H = max(max_H, H[y - 1])
#     ans = max(ans, max_H + G[y])
# print(ans + sum(C))
# print(D, E, F, G, H)


# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# ans = sum(C)
# print(ans)

# D, E, F, G, H = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)