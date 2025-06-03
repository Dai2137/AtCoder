from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

arrows = [[None] * W for _ in range(H)]
INF = 10 ** 18
dist = [[INF] * W for _ in range(H)]
que = deque()

for i in range(H):
    for j in range(W):
        if S[i][j] == 'E':
            que.append((i, j ))
            dist[i][j] = 0
            arrows[i][j] = 'E'
        elif S[i][j] == '#':
            arrows[i][j] = '#'

dirs = [(-1, 0, 'v'), (1, 0, '^'), (0, -1, '>'), (0, 1, '<')]

while que:
    i, j = que.popleft()
    for di, dj, arr in dirs:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= H or nj < 0 or nj >= W:
            continue
        if S[ni][nj] == '#':
            continue
        if dist[ni][nj] != INF:
            continue
        dist[ni][nj] = dist[i][j] + 1
        arrows[ni][nj] = arr
        que.append((ni, nj))

for i in range(H):
    print(''.join(arrows[i]))


    


