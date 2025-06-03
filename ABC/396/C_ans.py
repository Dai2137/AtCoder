N, M = map(int, input().split())

B = list(map(int, input().split()))
W = list(map(int, input().split()))

B.sort(reverse=True)
W.sort(reverse=True)

# 累積和を１回前計算する
 
# sumb = [0] * (N + 1)
# sumw = [0] * (M + 1)
# summaxw = [0] * (M + 1)

# for i in range(N):
#     sumb[i + 1] = sumb[i] + B[i]

# for i in range(M):
#     sumw[i + 1] = sumw[i] + W[i]
#     summaxw[i + 1] = max(summaxw[i], sumw[i + 1])

# ans = 0
# for i in range(N + 1):
    # ans = max(ans, sumb[i] + summaxw[min(i, M)])

# 一気にできる
sumb, sumw, maxw, ans = 0, 0, 0, 0

for i in range(N):
    sumb += B[i]
    if i < M:
        sumw += W[i]
        maxw = max(maxw, sumw)
    ans = max(ans, sumb + maxw)


print(ans)


    
