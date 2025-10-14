N = int(input())

A = [0] * (N+1)
A[0] = 1

S = 1

for i in range(1, N + 1):
    A[i] = S
    a = 0
    b = S
    while b > 0:
        a += b % 10
        b //= 10
    S += a

print(A[N])