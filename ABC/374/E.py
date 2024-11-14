N, X = map(int,input().split())
A, P, B, Q = [], [], [], []

for _ in range(N):
    a, p, b, q = map(int,input().split())
    A.append(a)
    P.append(p)
    B.append(b)
    Q.append(q)

def w2minX(w):
    minX = 0
    for i in range(N):
        if P[i]*B[i] < Q[i]*A[i]:
            minX_i = 10**10
            for B_num in range(A[i]):
                minX_i = min(minX_i, B_num * Q[i] + (max((w - B_num * B[i]), 0) + A[i] - 1) // A[i] * P[i] )
        else:
            minX_i = 10**10
            for A_num in range(B[i]):
                minX_i = min(minX_i, A_num * P[i] + (max((w - A_num * A[i]), 0) + B[i] - 1) // B[i] * Q[i] )
        minX += minX_i
            
    return minX

ok, ng = 0, 10**10

while ok + 1 < ng:
    mid = (ok + ng) // 2
    if w2minX(mid) <= X:
        ok = mid
    else:
        ng = mid
print(ok)

