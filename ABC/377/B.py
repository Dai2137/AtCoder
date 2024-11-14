S = []

for i in range(8):
    S.append(input())

isvoid = [[True] *8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if S[i][j]=="#":
            for ii in range(8):
                isvoid[ii][j] = False
            for jj in range(8):
                isvoid[i][jj] = False

ans = 0
for i in range(8):
    for j in range(8):
        ans += isvoid[i][j]

print(ans)