H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

def calc_xor(domino, A):
    xor_sum = 0
    for i in range(H):
        for j in range(W):
            if not domino[i][j]:
                xor_sum ^= A[i][j]
    return xor_sum

domino = [[False] * W for _ in range(H)]

ans = 0
def dfs(i, j, domino):
    global ans
    
    if j == W:
        i += 1
        j = 0
    
    if i == H:
        ans = max(ans, calc_xor(domino, A))
        return
    if domino[i][j]:
        dfs(i, j + 1, domino)
    else:
        dfs(i, j + 1, domino)
        if j + 1 < W and not domino[i][j + 1]:
            domino[i][j] = True
            domino[i][j + 1] = True
            dfs(i, j + 1, domino)
            domino[i][j] = False
            domino[i][j + 1] = False
        if i + 1 < H and not domino[i + 1][j]:
            domino[i][j] = True
            domino[i + 1][j] = True
            dfs(i, j + 1, domino)
            domino[i][j] = False
            domino[i + 1][j] = False
        
dfs(0, 0, domino)
print(ans)
