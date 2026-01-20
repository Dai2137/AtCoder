import heapq
N, K, X = map(int, input().split())
A = list(map(int, input().split()))
INF = 10 ** 18
A.sort(reverse=True)

hq = [(-A[0] * K, [K] + [0] * (N - 1), 0)]
heapq.heapify(hq)
# visited = set()
# visited.add(tuple([K] + [0] * (N - 1)))

for _ in range(X):
    cnt, state, tail = heapq.heappop(hq)
    print(- cnt)
    if tail > 0 and state[tail - 1] > 0:
        new_state = state[:]
        new_state[tail - 1] -= 1
        new_state[tail] += 1
        new_cnt = - (-cnt - A[tail - 1] + A[tail])
        heapq.heappush(hq, (new_cnt, new_state, tail))
    if tail < N - 1:
        new_state = state[:]
        new_state[tail] -= 1
        new_state[tail + 1] += 1
        new_cnt = - (-cnt - A[tail] + A[tail + 1])
        heapq.heappush(hq, (new_cnt, new_state, tail + 1))
