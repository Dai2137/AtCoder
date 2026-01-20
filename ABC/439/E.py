from bisect import bisect_left
N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda x: (x[0], -x[1]))
dp = []

for a, b in AB:
    pos = bisect_left(dp, b)
    if pos == len(dp):
        dp.append(b)
    else:
        dp[pos] = b

print(len(dp))










# import sys
# from bisect import bisect_left

# N = int(input())
# seg = [tuple(map(int, input().split())) for _ in range(N)]

# # A 昇順、A 同値は B 降順
# seg.sort(key=lambda x: (x[0], -x[1]))

# dp = []  # dp[len-1] = 長さlenのLISの末尾Bの最小値
# for a, b in seg:
#     pos = bisect_left(dp, b)  # strict increasing のため >=b を置換
#     if pos == len(dp):
#         dp.append(b)
#     else:
#         dp[pos] = b

# print(len(dp))

