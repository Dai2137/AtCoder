import heapq

N = int(input())

a = []
# v = []
for i in range(N):
    L, D = map(int, input().split())
    R = L + D
    a.append((L, R))
    # v.append(R)
a.sort()

# R_last = max(v)

q = []
heapq.heapify(q)

t = 0
# 優先度付きキューに入れるアイテム
ai = 0
# t_last = v[]
ans = 0
while ai < N or len(q) != 0:
        
    while ai < N and a[ai][0] == t:
        heapq.heappush(q, a[ai][1])
        ai += 1
    
    while q and q[0] < t:
        heapq.heappop(q)
    
    if q:
        heapq.heappop(q)
        ans += 1
            
    if len(q) == 0 and ai < N:
        t = a[ai][0]
        # heapq.heappush(pq, v[ai][1])    
    else:
        t += 1
print(ans)