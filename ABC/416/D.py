from sortedcontainers import SortedList
T = int(input())

def solve():
    N, M = map(int, input().split())
    A  = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A = [A[i] % M for i in range(N)]
    B = [B[i] % M for i in range(N)]

    A.sort(reverse=True)
    B = SortedList(B)
    ans = 0
    for i in range(N):
        rest = M - A[i]
        idx = B.bisect_left(rest)
        if idx < len(B):
            ans += (A[i] + B[idx]) % M
            B.pop(idx)
        else:
            ans += (A[i] + B[-1]) % M
            B.pop()
    print(ans)
    

for _ in range(T):
    solve()

