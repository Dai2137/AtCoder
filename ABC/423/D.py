import heapq
N, K = map(int, input().split())
A, B, C = [], [], []

for i in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

ans = [-1] * N
t = 0
tot = 0
que = []

for i in range(N):
    t = max(t, A[i])
    while tot + C[i] > K:
        leave_t, c = heapq.heappop(que)
        tot -= c
        t = max(t, leave_t)
    ans[i] = t
    tot += C[i]
    heapq.heappush(que, (t + B[i], C[i]))
    
for i in range(N):
    print(ans[i])
