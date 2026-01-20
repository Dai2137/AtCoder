N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mod = 998244353
ans = N * sum(B) - M * sum(A)
# print(ans)
A.sort()
B.sort()
j = 0
tot = 0
for i in range(N):
    while j < M and A[i] >= B[j]:
        tot += B[j]
        j += 1
    left = A[i] * j
    right = tot
    ans += 2 * (left - right)

print(ans% mod)