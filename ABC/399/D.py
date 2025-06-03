T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(2 * N):
        A[i] -= 1
    
    idxs = [[] for i in range(N)]
    for i in range(2 * N):
        idxs[A[i]].append(i)
    cnt = 0
    for i in range(2 * N - 1):
        if abs(idxs[A[i]][0] - idxs[A[i]][1]) < 2 or abs(idxs[A[i + 1]][0] - idxs[A[i + 1]][1]) < 2:
            continue
        
        if i == idxs[A[i]][1] or i + 1 == idxs[A[i + 1]][1]:
            continue
        
        if idxs[A[i]][1] + 1 == idxs[A[i + 1]][1] or idxs[A[i]][1] - 1 == idxs[A[i + 1]][1]:
            cnt += 1
    print(cnt)
    
    

