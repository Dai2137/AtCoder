# import math
T = int(input())

def s(n:int) -> int:
    ok, ng = 0, n
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if mid * mid <= n:
            ok = mid
        else:
            ng = mid
    return ok

def S(l: int, r: int) -> int:
    return s(r) - s(l - 1)

def g(C: int, r: int) -> int:
    res = 0
    for d in range(1, 11):
        base = C * 10 ** d
        nl, nr = base + 10 ** (d - 1), base + 10 ** d - 1
        nr = min(nr, base + r)
        if nr < nl:
            return res
        res += S(nl, nr)
    return res

for _ in range(T):
    C, D = map(int, input().split())
    ans = g(C, C + D) - g(C, C)
    print(ans)