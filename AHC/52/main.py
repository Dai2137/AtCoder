import os
from collections import deque

# -------------------------
# 入力: v, h から壁情報を構築
# -------------------------
def build_cell_walls(v, h, N):
    cell_walls = [[{"U":False,"D":False,"L":False,"R":False} for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if j == 0: cell_walls[i][j]["L"] = True
            if j == N-1: cell_walls[i][j]["R"] = True
            if i == 0: cell_walls[i][j]["U"] = True
            if i == N-1: cell_walls[i][j]["D"] = True
            if j < N-1 and v[i][j] == '1':
                cell_walls[i][j]["R"] = True
                cell_walls[i][j+1]["L"] = True
            if i < N-1 and h[i][j] == '1':
                cell_walls[i][j]["D"] = True
                cell_walls[i+1][j]["U"] = True
    return cell_walls

# -------------------------
# BFS で最短経路
# -------------------------
def bfs_path(start, goal, walls, H, W):
    dirs = [(-1,0,"U"), (1,0,"D"), (0,-1,"L"), (0,1,"R")]
    rev = {"U":"D","D":"U","L":"R","R":"L"}
    dist = [[-1]*W for _ in range(H)]
    parent, move = {}, {}
    q = deque([start])
    dist[start[0]][start[1]] = 0
    while q:
        x,y = q.popleft()
        if (x,y) == goal: break
        for dx,dy,cmd in dirs:
            nx,ny = x+dx,y+dy
            if 0<=nx<H and 0<=ny<W:
                if walls[x][y][cmd]: continue
                if walls[nx][ny][rev[cmd]]: continue
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y]+1
                    parent[(nx,ny)] = (x,y)
                    move[(nx,ny)] = cmd
                    q.append((nx,ny))
    if dist[goal[0]][goal[1]] == -1:
        return None
    path, cur = [], goal
    while cur != start:
        path.append(move[cur])
        cur = parent[cur]
    return path[::-1]

# -------------------------
# 全域掃き
# -------------------------
def sweep_all(H, W, walls, start=(0,0)):
    visited = [[False]*W for _ in range(H)]
    ops, x, y = [], start[0], start[1]
    visited[x][y] = True
    def all_visited(): return all(all(row) for row in visited)
    while not all_visited():
        moved = False
        for dx,dy,cmd in [(-1,0,"U"), (1,0,"D"), (0,-1,"L"), (0,1,"R")]:
            nx,ny = x+dx,y+dy
            if 0<=nx<H and 0<=ny<W:
                if not visited[nx][ny]:
                    if not walls[x][y][cmd] and not walls[nx][ny][{"U":"D","D":"U","L":"R","R":"L"}[cmd]]:
                        ops.append(cmd); x,y = nx,ny
                        visited[x][y] = True; moved = True; break
        if moved: continue
        targets = [(i,j) for i in range(H) for j in range(W) if not visited[i][j]]
        if not targets: break
        targets.sort(key=lambda t: abs(t[0]-x)+abs(t[1]-y))
        path = None
        for t in targets:
            path = bfs_path((x,y), t, walls, H, W)
            if path: break
        if not path: break
        for cmd in path:
            if cmd=="U": x-=1
            if cmd=="D": x+=1
            if cmd=="L": y-=1
            if cmd=="R": y+=1
            ops.append(cmd); visited[x][y] = True
    return "".join(ops)

# -------------------------
# in フォルダを一括処理
# -------------------------
IN_DIR = "in"
OUT_DIR = "out"
os.makedirs(OUT_DIR, exist_ok=True)

for fname in os.listdir(IN_DIR):
    if not fname.endswith(".txt"): continue
    with open(os.path.join(IN_DIR, fname)) as f:
        N, M, K = map(int, f.readline().split())
        robot_position = [[None]*M for _ in range(2*N**2)]
        for k in range(M):
            i,j = map(int, f.readline().split())
            robot_position[0][k] = (i,j)
        v = [f.readline().strip() for _ in range(N)]
        h = [f.readline().strip() for _ in range(N-1)]
    walls = build_cell_walls(v,h,N)
    path = sweep_all(N,N,walls,(0,0))

    # --- ロボット行動行列 c ---
    c = [["S"] * M for _ in range(K)]   # デフォルトは待機 S
    for t, cmd in enumerate(path[:K]):  # K ステップ分だけ
        c[t][0] = cmd                   # ロボット0に操作を
