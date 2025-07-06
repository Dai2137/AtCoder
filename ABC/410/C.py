N, Q = map(int, input().split())
temp = 0

A = []
for i in range(N):
    A.append(i + 1)

for _ in range(Q):
    px = list(map(int, input().split()))
    if px[0] == 1:
        p, x = px[1], px[2]
        p -= 1
        p += temp
        p %= N
        A[p] = x
    elif px[0] == 2:
        p = px[1]
        p -= 1
        p += temp
        p %= N
        print(A[p])
    else:
        k = px[1]
        temp += k
        

