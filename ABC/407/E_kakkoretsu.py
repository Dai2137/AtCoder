import heapq

T = int(input())

def solve():
    N = int(input())
    A = []
    for _ in range(2 * N):
        A.append(int(input()))
        
    hq = []
    heapq.heapify(hq)
    
    ans = A[0]
    for i in range(1, 2 * N - 1, 2):
        heapq.heappush(hq, - A[i])
        heapq.heappush(hq, - A[i + 1])
        ans -= heapq.heappop(hq)
    print(ans)

for _ in range(T):
    solve()
    
# gitの勉強用に変更
