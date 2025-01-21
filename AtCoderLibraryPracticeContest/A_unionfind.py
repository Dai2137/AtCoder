from atcoder.dsu import DSU

N, Q = map(int, input().split())

uf = DSU(N)

for _ in range(Q):
    t, u, v = map(int, input().split())
    if t == 0:
        uf.merge(u, v)
    else:
        if uf.same(u, v):
            print(1)
        else:
            print(0)