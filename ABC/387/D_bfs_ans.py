from collections import deque
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == 'S':
            S_idx = (i, j)
        elif S[i][j] == 'G':
            G_idx = (i, j)


INF = 10**10
ans = INF
ans_temp = INF

moves = [
    [(1,0), (-1,0)], 
    [(0,1), (0, -1)]
]

for p in range(2):
    dist = [[INF] * W for _ in range(H)]
    dist[S_idx[0]][S_idx[1]] = 0
    visited = deque([S_idx])

    while visited:
        x, y = visited.popleft()
        if (x, y) == G_idx:
            ans_temp = dist[G_idx[0]][G_idx[1]]
            break
        
        for dx, dy in moves[(x + y + p) % 2]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and S[nx][ny]!='#' and dist[nx][ny]==INF:
                dist[nx][ny] = dist[x][y] + 1
                visited.append((nx, ny))
        
    ans = min(ans, ans_temp)

print('-1' if ans==INF else ans)