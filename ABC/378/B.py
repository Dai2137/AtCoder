N = int(input())
q = [0] * N
r = [0] * N

for i in range(N):
    q[i], r[i] = map(int, input().split())

Q = int(input())

for _ in range(Q):
    t, d = map(int, input().split())
    t -= 1
    if d % q[t] <= r[t]:
        print(d // q[t] * q[t] + r[t])
    else:
        print((d // q[t] + 1) * q[t] + r[t])
