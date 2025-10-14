import heapq
Q = int(input())
a = []
heapq.heapify(a)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        heapq.heappush(a, x)
    else:
        print(heapq.heappop(a))
    
