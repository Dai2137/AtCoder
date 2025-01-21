S = input()
Q = int(input())
K = list(map(int, input().split()))
for i in range(Q):
    K[i] -= 1 

C = [None] * Q
N = len(S)

for i in range(Q):
    inv = False
    while K[i] >= N:
        for j in range(70):
            if K[i] < N * (2 ** j):
                break
        K[i] -= N * 2 ** (j - 1)
        inv = not inv
    if inv:
        C[i] = S[K[i]].swapcase()
    else:
        C[i] = S[K[i]]
print(*C)