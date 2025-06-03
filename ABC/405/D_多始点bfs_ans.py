from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

# 結果として各マスに進むべき矢印を記録する配列
arrow = [[''] * W for _ in range(H)]

# BFS用の初期キューに非常口 'E' を全部入れる
queue = deque()
dist = [[-1] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == 'E':
            queue.append((i, j))
            dist[i][j] = 0  # 非常口の距離は0
            arrow[i][j] = 'E'  # 非常口はそのまま

# 逆向きの方向 → 今のマスからどちらに行けば次に進めるか
# 通常の方向: (di, dj) に対して、逆に来たときは (-di, -dj)
# つまり、次に進むべき方向は逆に設定する
dirs = [(-1, 0, 'v'), (1, 0, '^'), (0, -1, '>'), (0, 1, '<')]

while queue:
    i, j = queue.popleft()
    for di, dj, d_char in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W:
            if S[ni][nj] == '.' and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                arrow[ni][nj] = d_char  # このマスにいるとき、どちらに進むべきか
                queue.append((ni, nj))

# 出力（壁 '#' と 非常口 'E' はそのまま）
for i in range(H):
    line = ''
    for j in range(W):
        if S[i][j] == '#':
            line += '#'
        elif S[i][j] == 'E':
            line += 'E'
        else:
            line += arrow[i][j]
    print(line)
