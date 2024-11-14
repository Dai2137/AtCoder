N,M = map(int,input().split())
X = list(map(lambda x: int(x) - 1, input().split()))
A = list(map(int,input().split()))
XA = []
for i in range(M):
    XA.append((X[i], A[i]))
XA.sort()
for i in range(M):
    X[i], A[i] = XA[i]
if sum(A) != N:
    print(-1)
    exit()
# shakkin = 0
# print("a")
t = N-1
ans = 0
for i in reversed(range(M)):
    s = t - A[i] + 1
    # print(s,t,X[i])
    if s < X[i]:
        print(-1)
        exit()
    ans += (s + t - 2 * X[i]) * A[i] // 2
    # shakkin = s - X[i]
    t = s - 1
    # print(s,t)
print(ans)