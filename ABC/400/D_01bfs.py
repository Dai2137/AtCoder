
# https://www.youtube.com/live/xukpZfJ0NNUで01-BFS,dijkstraの関係を説明している
# https://atcoder.jp/contests/abc246/editorial/3702に01-BFSの詳細な説明がある
from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
A, B, C, D = map(int, input().split())

A -= 1; B -= 1; C -= 1; D -= 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

INF = 10**9
dist = [[INF] * W for _ in range(H)]
dist[A][B] = 0

que = deque()
que.append((A, B))

while que:
    x, y = que.popleft()

    for i in range(4):
        # 1マス先
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < H and 0 <= ny < W:
            if S[nx][ny] == '.' and dist[nx][ny] > dist[x][y]:
                dist[nx][ny] = dist[x][y]
                que.appendleft((nx, ny))
            elif S[nx][ny] == '#' and dist[nx][ny] > dist[x][y] + 1:
                dist[nx][ny] = dist[x][y] + 1
                que.append((nx, ny))

        # 2マス先
        nx2 = x + dx[i]*2
        ny2 = y + dy[i]*2
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= nx2 < H and 0 <= ny2 < W:
            # 中間と2マス先が壁である必要あり（2つ壊せる）
            if S[mx][my] == '#' and S[nx2][ny2] == '#' and dist[nx2][ny2] > dist[x][y] + 1:
                dist[nx2][ny2] = dist[x][y] + 1
                que.append((nx2, ny2))
            elif S[mx][my] == '#' and S[nx2][ny2] == '.' and dist[nx2][ny2] > dist[x][y] + 1:
                dist[nx2][ny2] = dist[x][y] + 1
                que.append((nx2, ny2))

print(dist[C][D] if dist[C][D] != INF else -1)
