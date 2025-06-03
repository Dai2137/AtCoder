N, W = map(int, input().split())

YXi = []
for i in range(N):
    X, Y = map(int, input().split())
    X-=1
    Y-=1
    YXi.append((Y, X, i))

YXi.sort()

r = [0] * N
num = [0] * W
for idx in range(N):
    r[YXi[idx][2]] = num[YXi[idx][1]]
    num[YXi[idx][1]] += 1

r_max = max(r)
d = [-1] * (r_max + 1)
cnt = [0] * (r_max + 1)
for idx in range(N):
    d[r[YXi[idx][2]]] = max(d[r[YXi[idx][2]]], YXi[idx][0] + 1)
    cnt[r[YXi[idx][2]]] += 1

for i in range(r_max + 1):
    if cnt[i] < W:
        d[i] = 10 ** 10

Q = int(input()) 
for q in range(Q):
    T, A = map(int, input().split())
    A -= 1
    if T < d[r[A]]:
        print("Yes")
    else:
        print("No")

# print(d)
# print(r)