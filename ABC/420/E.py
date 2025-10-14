from atcoder.dsu import DSU

N, Q = map(int, input().split())

uf = DSU(N)
is_black = [False] * N
s = [0] * N

for _ in range(Q):
    tuv = list(map(int, input().split()))
    if tuv[0] == 1:
        u, v = tuv[1] - 1, tuv[2] - 1
        u, v = uf.leader(u), uf.leader(v)
        if u == v:
            continue
        uf.merge(u, v) 
        w = uf.leader(u)
        s[w] = s[u] + s[v]
        s[w ^ u ^ v] = 0
    elif tuv[0] == 2:
        v = tuv[1] - 1
        if is_black[v]:
            s[uf.leader(v)] -= 1
            is_black[v] = False
        else:
            s[uf.leader(v)] += 1
            is_black[v] = True
        
    else:
        v = tuv[1] - 1
        print("Yes" if s[uf.leader(v)] else "No")
