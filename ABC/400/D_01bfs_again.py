from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

A, B, C, D = map(int, input().split())

A -= 1
B -= 1
C -= 1
D -= 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
INF = 10**9

dist = [[INF] * W for _ in range(H)]
visited = [[False] * W for _ in range(H)]

dist[A][B] = 0
visited[A][B] = True

que = deque()
que.append((A, B))

while que:
    x, y = que.popleft()
    visited[x][y] = True
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W:
            if visited[nx][ny]:
                continue
            if S[nx][ny] == '.' and dist[nx][ny] > dist[x][y]:
                dist[nx][ny] = dist[x][y]
                que.appendleft((nx, ny))
    
    for i in range(4):
        for j in range(1,3):
            nx, ny = x + j * dx[i], y + j * dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if visited[nx][ny]:
                    continue
                if S[nx][ny] == '#' and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    que.append((nx, ny))

print(dist[C][D])
    