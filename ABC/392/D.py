N = int(input())

K = []
A = []

for i in range(N):
    KA = list(map(int, input().split()))
    K.append(KA[0])
    A.append(KA[1:])

# D[i]：サイコロiの目のカウント
D = [None] * N

for i in range(N):
    D[i] = {}
    for Ai in A[i]:
        if Ai not in D[i]:
            D[i][Ai] = 0
        D[i][Ai] += 1

ans = 0.0

for i in range(N):
    for j in range(i + 1, N):
        temp = 0.0
        for Di in D[i]:
            if Di in D[j]:
                temp += D[i][Di] * D[j][Di]
        temp /= (len(A[i]) * len(A[j]))
        ans = max(ans, temp)
print(ans)