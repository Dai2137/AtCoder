N, M = map(int, input().split())

A, B = [], []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a - 1)
    B.append(b)


S = [[] for _ in range(M)]

for i in range(N):
    S[A[i]].append(B[i])

for i in range(M):
    print(sum(S[i]) / len(S[i]))
    
    