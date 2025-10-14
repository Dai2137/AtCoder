N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
min_A_B = []

for i in range(N):
    if A[i] < B[i]:
        min_A_B.append([0, A[i]])
    else:
        min_A_B.append([1, B[i]])
    ans += min(A[i], B[i])

for _ in range(Q):
    c, X, V = input().split()
    X = int(X) - 1
    V = int(V)
    
    if c == 'A':
        if min_A_B[X][0] == 0:
            if V < B[X]:
                ans += V - min_A_B[X][1]
                min_A_B[X][1] = V
            else:
                ans += B[X] - min_A_B[X][1]
                min_A_B[X][1] = B[X]
                min_A_B[X][0] = 1
        else:
            if V < B[X]:
                ans += V - min_A_B[X][1]
                min_A_B[X][1] = V
                min_A_B[X][0] = 0
        A[X] = V
    else:
        if min_A_B[X][0] == 1:
            if V < A[X]:
                ans += V - min_A_B[X][1]
                min_A_B[X][1] = V
            else:
                ans += A[X] - min_A_B[X][1]
                min_A_B[X][1] = A[X]
                min_A_B[X][0] = 0
        else:
            if V < A[X]:
                ans += V - min_A_B[X][1]
                min_A_B[X][1] = V
                min_A_B[X][0] = 1
        B[X] = V
    print(ans)
