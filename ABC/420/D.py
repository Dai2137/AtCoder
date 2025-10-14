from collections import deque

H, W = map(int, input().split())
A = [input() for _ in range(H)]

visited = [[[False] * 2 for _ in range(W)] for _ in range(H)]
dist = [[[0] * 2 for _ in range(W)] for _ in range(H)]
que = deque()

for i in range(H):
    for j in range(W):
        if A[i][j] == 'S':
            start = (i, j)
            visited[i][j][0] = True
            que.append((i, j, 0))
        elif A[i][j] == 'G':
            goal = (i, j)

while que:
    i, j, k = que.popleft()
    if (i, j) == goal:
        print(dist[i][j][k])
        exit()
    
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= H or nj < 0 or nj >= W:
            continue
        if A[ni][nj] == '#':
            continue
        if A[ni][nj] == 'o' and k == 1:
            continue
        if A[ni][nj] == 'x' and k == 0:
            continue

        if A[ni][nj] != '?':
            if visited[ni][nj][k]:
                continue
            visited[ni][nj][k] = True
            dist[ni][nj][k] = dist[i][j][k] + 1
            que.append((ni, nj, k))
        else:
            if visited[ni][nj][1 - k]:
                continue
            visited[ni][nj][1 - k] = True
            dist[ni][nj][1 - k] = dist[i][j][k] + 1
            que.append((ni, nj, 1 - k))

print(-1)
