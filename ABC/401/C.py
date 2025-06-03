N, K = map(int, input().split()) 
if N < K:
    print('1')
    exit()

A = [0] * (N + 1)
for i in range(K):
    A[i] = 1

A[K] = K

for i in range(K + 1, N + 1):
    A[i] = (2 * A[i - 1] - A[i - K - 1]) % 1000000000

print(A[N])