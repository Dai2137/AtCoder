from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))

ft = FenwickTree(N)

for i in range(N):
    ft.add(i, A[i])

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1] - 1
        ft.add(x, A[x + 1] - A[x])
        ft.add(x + 1, A[x] - A[x + 1])
        A[x], A[x + 1] = A[x + 1], A[x]
        
    else:
        l, r = query[1] - 1, query[2] - 1
        print(ft.sum(l, r + 1))
