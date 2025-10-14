from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
tot = sum(A)
max_a = max(A)
A.sort()
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]


def solve():
    b = int(input())
    if b > max_a:
        print(-1)
        return
    a = 0
    idx = bisect_left(A, b - 1)
    a += S[idx]
    a += (N - idx) * (b - 1)
    print(min(a + 1, tot))

for _ in range(Q):
    solve()
    
