N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
w = A[0] * Y
ans = 0

for i in range(N):
    max_w = A[i] * Y
    sabun = max_w - w
    if sabun % (Y - X) != 0:
        print(-1)
        exit()
    num_X = sabun // (Y - X)
    num_Y = (w - num_X * X) // Y
    if num_X < 0 or num_Y < 0:
        print(-1)
        exit()
    ans += num_Y


print(ans)
