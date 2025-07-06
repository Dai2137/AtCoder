T = int(input())

def sort_P(N, P):
    if N == 1:
        return sorted(P)
    else:
        P_former = P[:2 ** (N - 1)]
        P_latter = P[2 ** (N - 1):]
        P_former = sort_P(N - 1, P_former)
        P_latter = sort_P(N - 1, P_latter)
        if P_former[0] < P_latter[0]:
            return P_former + P_latter
        else:
            return P_latter + P_former


def solve():
    N = int(input())
    P = list(map(int, input().split()))
    P = sort_P(N, P)
    print(*P)

for _ in range(T):
    solve()
