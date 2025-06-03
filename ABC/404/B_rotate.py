def rotate_90_clockwise(S):
    H = len(S)
    W = len(S[0])
    return [[S[H - 1 - j][i] for j in range(H)] for i in range(W)]

N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]
ans = 10 ** 10
for i in range(4):
    cnt = i
    Si = S.copy()
    for _ in range(i):
        Si = rotate_90_clockwise(Si)
    if i == 0:
        Si = S
    for j in range(N):
        for k in range(N):
            if Si[j][k] != T[j][k]:
                cnt += 1
    ans = min(ans, cnt)
print(ans)
    
