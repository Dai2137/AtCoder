# N = int(input())

# U, D, L, R = [], [], [], []

# for _ in range(N):
#     u, d, l, r = map(int, input().split())
#     U.append(u-1)
#     D.append(d-1)
#     L.append(l-1)
#     R.append(r-1)

# diff = [[0] * (2001) for _ in range(2001)]

# for i in range(N):
#     diff[U[i]][L[i]] += 1
#     diff[U[i]][R[i] + 1] -= 1
#     diff[D[i] + 1][L[i]] -= 1
#     diff[D[i] + 1][R[i] + 1] += 1

# for i in range(1, 2001):
#     for j in range(1, 2001):
#         diff[i][j] += diff[i][j - 1]

# for i in range(1, 2001):
#     for j in range(1, 2001):
#         diff[i][j] += diff[i - 1][j]

# cnt = diff.copy()
# zero = 0

# for i in range(1, 2001):
#     for j in range(1, 2001):
#         if cnt[i][j] == 0:
#             zero += 1

# one = [[0] * (2001) for _ in range(2001)]

# for i in range(1, 2001):
#     for j in range(1, 2001):
#         if cnt[i][j] == 1:
#             one[i][j] = 1

# # S = [[0] * (2001) for _ in range(2001)]

# for i in range(1, 2001):
#     for j in range(1, 2001):
#         one[i][j] += one[i][j - 1]

# for i in range(1, 2001):
#     for j in range(1, 2001):
#         one[i][j] += one[i - 1][j]

# S = one.copy()

# for i in range(N):
#     cnt_one = S[D[i]][R[i]] - S[D[i]][L[i] - 1] - S[U[i] - 1][R[i]] + S[U[i] - 1][L[i] - 1]
#     print(zero + cnt_one)


import sys
input = sys.stdin.readline

N = int(input())
U, D, L, R = [], [], [], []

for _ in range(N):
    u, d, l, r = map(int, input().split())
    U.append(u-1)
    D.append(d-1)
    L.append(l-1)
    R.append(r-1)

# いもす用 2001 x 2001
diff = [[0]*2001 for _ in range(2001)]

for i in range(N):
    diff[U[i]][L[i]] += 1
    diff[U[i]][R[i]+1] -= 1
    diff[D[i]+1][L[i]] -= 1
    diff[D[i]+1][R[i]+1] += 1

# 横方向累積（ j = 0 から！）
for i in range(2001):
    for j in range(1, 2001):
        diff[i][j] += diff[i][j-1]

# 縦方向累積（ i = 0 から！）
for i in range(1, 2001):
    for j in range(2001):
        diff[i][j] += diff[i-1][j]

# cnt = diff の深いコピー
cnt = [row[:] for row in diff]

# zero count
zero = 0
for i in range(2000):
    for j in range(2000):
        if cnt[i][j] == 0:
            zero += 1

# cnt == 1 を one に
one = [[0]*2001 for _ in range(2001)]
for i in range(2000):
    for j in range(2000):
        if cnt[i][j] == 1:
            one[i][j] = 1

# 2D 累積 S
for i in range(2001):
    for j in range(1, 2001):
        one[i][j] += one[i][j-1]

for i in range(1, 2001):
    for j in range(2001):
        one[i][j] += one[i-1][j]

S = one  # もう deep copy 済み

def rect_sum(u, d, l, r):
    if u > d or l > r:
        return 0
    return S[d][r] - (S[u-1][r] if u > 0 else 0) \
                   - (S[d][l-1] if l > 0 else 0) \
                   + (S[u-1][l-1] if u > 0 and l > 0 else 0)

# 各雲 k を除いたときの answer
for k in range(N):
    cnt_one = rect_sum(U[k], D[k], L[k], R[k])
    print(zero + cnt_one)
