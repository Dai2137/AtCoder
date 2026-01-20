N, M = map(int, input().split())

nurarekata = set()

S = [list(input()) for _ in range(N)]


for s_i in range(N-M+1):
    for s_j in range(N-M+1):
        masu = tuple(tuple(S[i][j] for j in range(s_j, s_j + M)) for i in range(s_i, s_i + M))
        nurarekata.add(masu)
        print(masu)

print(len(nurarekata))
