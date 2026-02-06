T = int(input())

for _ in range(T):
    N = int(input())
    R = list(map(int, input().split()))

    L = [0] * N
    G = [0] * N

    L[0] = R[0]
    for i in range(1, N):
        L[i] = min(R[i], L[i - 1] + 1)

    G[N - 1] = R[N - 1]
    for i in range(N - 2, -1, -1):
        G[i] = min(R[i], G[i + 1] + 1)

    ans = 0
    for i in range(N):
        h = L[i] if L[i] < G[i] else G[i]
        ans += R[i] - h

    print(ans)
