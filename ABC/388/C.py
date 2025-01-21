# # 二分探索
# from bisect import bisect_left
# N = int(input())
# A = list(map(int,input().split()))

# ans = 0

# for i in range(N):
#     ans += N - bisect_left(A, 2 * A[i])
# print(ans)

# 尺取法
N = int(input())
A = list(map(int,input().split()))

ans = 0
j = 0
for i in range(N):
    while j < N and A[j] * 2 <= A[i]:
        j += 1
    ans += j
print(ans)