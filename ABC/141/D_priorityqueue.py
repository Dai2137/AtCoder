import heapq

N,M = map(int,input().split())
A = list(map(int, input().split()))

A = list(map(lambda x: x*(-1), A))
heapq.heapify(A)

for _ in range(M):
  maxA = heapq.heappop(A)
  heapq.heappush(A, ((-maxA)//2 * (-1)))
  # print(A)

print(-sum(A))