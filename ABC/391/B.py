N, M = map(int,input().split())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(M)]

# print(S)
# print(T)
for a in range(N-M+1):
    for b in range(N-M+1):
        flag = True
        for i in range(M):
            for j in range(M):
                if T[i][j] != S[i + a][j + b]:
                    flag = False
        if flag:
            print(a+1)
            print(b+1)