from itertools import product
N, K, X = map(int, input().split())

S = [input() for _ in range(N)]
# S.sort()
# # print(S)
# ans = ""
# X -= 1
# for i in range(K - 1, -1, -1):
#     # print(X//(N ** i) % N)
#     ans += S[X//(N ** i) % N]

list = list(range(N))
C = []
for A in product(list, repeat=K):
    f = []
    for i in range(K):
        f.append(S[A[i]])
    C.append(''.join(f))

C.sort()

print(C[X - 1])

