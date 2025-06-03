# N, X = map(int,input().split())

# vac = [[] for i in range(3)]

# for i in range(N):
#     V, A, C = map(int,input().split())
#     V-=1
#     vac[V].append((A, C))

# # dp[i][j][k]-> ビタミンiを,食べ物jまで考えて，カロリーk以下で摂取できる最大値
# dp = [[[0] * 5002 for l in range(5002)] for _ in range(3)]

# # for i in range(3):
# #     dp[i][0][0] = 0

# for i in range(3):
#     for j in range(len(vac[i])):
#         for k in range(5002):
#             if j - 1 >= 0 and k - vac[i][j][1] >= 0:
#                 dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - vac[i][j][1]] + vac[i][j][0])
#             if j - 1 >= 0:
#                 dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k])

# T = [[0] * 5002 for i in range(3)]

# for i in range(3):
#     for k in range(5002):
#         for j in range(len(vac[i])):
#             T[i][k] = max(T[i][k], dp[i][j][k])

# ans = 0

# for i in range(X + 1):
#     for j in range(X - i + 1):
#         if X - i - j >= 0:
#             ans = max(ans, min(T[0][i], T[1][j], T[2][X - i - j]))


# print(vac)
# # print(dp)


        
N, X = map(int, input().split())

# 3種類のビタミンごとに分類
vac = [[] for _ in range(3)]

for _ in range(N):
    V, A, C = map(int, input().split())
    V -= 1  # 0-indexed に変換
    vac[V].append((A, C))  # (ビタミン量, カロリー)

# DPテーブル dp[i][k]: ビタミン i を摂取するとき、カロリー k 以下で得られる最大ビタミン量
dp = [[0] * 5002 for _ in range(3)]

# 各ビタミンについて 0-1 ナップサックを適用
for i in range(3):
    for A, C in vac[i]:  # 食品ごとに DP を更新
        for k in range(5001, C - 1, -1):  # 大きい順に更新（0-1ナップサック）
            dp[i][k] = max(dp[i][k], dp[i][k - C] + A)

# 3種類のビタミンを X カロリー以内で最大限バランスよく摂取する
ans = 0
for i in range(X + 1):
    for j in range(X - i + 1):
        k = X - i - j  # 残りのカロリー
        if k >= 0:
            ans = max(ans, min(dp[0][i], dp[1][j], dp[2][k]))

print(ans)
