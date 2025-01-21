# from collections import deque
from atcoder.dsu import DSU

H, W = map(int ,input().split())

S = [list(input()) for _ in range(H)]

didj = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
# ans = 0
used = [[False] * W for i in range(H)]

uf = DSU(W * H)

for i in range(H):
    for j in range(W):
        # if used[i][j]:
            # continue
        if S[i][j] == '#':
            for di, dj in didj:
                ni, nj = di + i, dj + j
                if 0 <= ni < H and 0 <= nj < W  and S[ni][nj] == '#':
                    # used[ni][nj] = True
                    uf.merge(W * i + j, W * ni + nj)
# print(uf.groups())

ufg = uf.groups()
ans = 0
for i in range(len(ufg)):
    if S[ufg[i][0] // W][ufg[i][0] % W] == '#':
       ans += 1 
       
print(ans)