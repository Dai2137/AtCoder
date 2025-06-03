H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = 0
domino = [[False] * W for _ in range(H)]

def calc_xor():
    res = 0
    for i in range(H):
        for j in range(W):
            if not domino[i][j]:
                res ^= A[i][j]
    return res

def dfs(i, j):
    global ans
    if j == W:
        i += 1
        j = 0
    if i == H:
        ans = max(ans, calc_xor())
        return
    if domino[i][j]:
        dfs(i, j + 1)
        return

    # 置かない
    dfs(i, j + 1)

    # 横に置けるか？
    if j + 1 < W and not domino[i][j + 1]:
        domino[i][j] = domino[i][j + 1] = True
        dfs(i, j + 2)
        domino[i][j] = domino[i][j + 1] = False

    # 縦に置けるか？
    if i + 1 < H and not domino[i + 1][j]:
        domino[i][j] = domino[i + 1][j] = True
        dfs(i, j + 1)
        domino[i][j] = domino[i + 1][j] = False

dfs(0, 0)
print(ans)
