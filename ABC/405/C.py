N = int(input())
A = list(map(int, input().split()))

tot = sum(A)

S = 0
for i in range(N):
    S += A[i] ** 2

print((tot ** 2 - S) // 2)
