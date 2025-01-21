from collections import deque
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == 'S':
            S_idx = (i, j)
        elif S[i][j] == 'G':
            G_idx = (i, j)

que = deque([(S_idx[0], S_idx[1], [(1,0),(-1,0),(0,1),(0,-1)])])

INF = 10**10
dist = [[INF] * W for _ in range(H)]
dist[S_idx[0]][S_idx[1]] = 0

ans = -1
while que:
    x, y, dxdy = que.popleft()
    if (x, y) == G_idx:
        ans = dist[x][y]
        break

    for dx, dy in dxdy:
        if 0 <= x + dx < H and 0 <= y + dy < W and S[x + dx][y + dy]!='#' and dist[x+dx][y+dy]==INF:        
            dist[x+dx][y+dy] = dist[x][y] + 1
            if (dx, dy) == (1,0) or (dx, dy) == (-1,0):
                que.append((x+dx, y+dy, [(0,1),(0,-1)]))
            else:
                que.append((x+dx, y+dy, [(1,0),(-1,0)]))
              
print(ans)