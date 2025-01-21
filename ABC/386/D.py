N, M = map(int, input().split())
# G = [[None] * N for _ in range(N)]
Y_min =  10**10
XYC = []
for _ in range(M):
    X, Y, C = input().split()
    X = int(X) - 1
    Y = int(Y) - 1
    # G[X][Y] = C
    XYC.append((X, Y, C))

XYC.sort()

ans = True
for X, Y, C in XYC:
    if C == "W":
        Y_min = min(Y_min, Y)
    else:
        if Y_min <= Y:
            ans = False

print("Yes" if ans else "No")




