from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
INF = 10 ** 18
A.append(INF)

def judge(r, X, Y, l):
    s = A[r] - (X - 1)
    s -= r - l
    return s <= Y
    
for _ in range(Q):
    X, Y = map(int, input().split())
    l = bisect_left(A, X)
    
    if A[l] - X >= Y:
        print(X + Y - 1)
        continue
    ok = l
    ng = N
    while ng - ok > 1:
        m = (ok + ng) // 2
        if judge(m, X, Y, l):
            ok = m
        else:
            ng = m

    ans = X + Y  - 1 + (ok - l + 1)
    print(ans)
