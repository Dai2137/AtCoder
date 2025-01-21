N, D = map(int, input().split())
T, L = [], []
for _ in range(N):
    Ti, Li = map(int,input().split())
    T.append(Ti)
    L.append(Li)

for k in range(1, D+1):
    m = -1
    for i in range(N):
        m = max(m, T[i] * (L[i] + k))
    print(m)
    