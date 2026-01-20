T = int(input())


def solve():
    N = int(input())
    W, P, cost  = [], [], []
    for i in range(N):
        w, p = map(int, input().split())
        W.append(w)
        P.append(p)
        cost.append(w + p)
    S = sum(P) 
    cost.sort()
    temp, ans = 0, 0
    for i in range(N):
        temp += cost[i]
        if temp > S:
            break
        ans += 1
    print(ans)
    

for _ in range(T):
    solve()