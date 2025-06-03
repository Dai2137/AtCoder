H, W = map(int,input().split())
S = [list(input()) for _ in range(H)]

b_i_min, b_i_max, b_j_min, b_j_max = 1002, -1, 1002, -1

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            b_i_min = min(b_i_min, i)
            b_j_min = min(b_j_min, j)
            b_i_max = max(b_i_max, i)
            b_j_max = max(b_j_max, j)

ans = True
for i in range(b_i_min, b_i_max + 1):
    for j in range(b_j_min, b_j_max + 1):
        if S[i][j] == '.':
            ans = False
            break
print("Yes" if ans else "No")        