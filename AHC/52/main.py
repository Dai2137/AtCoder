# N = 30
# M = 10
# K = 10

N, M, K = map(int, input().split())

# (時刻，ロボットid) -> i座標, j座標
robot_position = [[None] * M for _ in range(2 * N ** 2)]

# 初期位置ロボットの座標を取得
for k in range(M):
    i, j = map(int, input().split())
    robot_position[0][k] = (i, j)

# 壁の座標を取得
v = [input() for _ in range(N)]
h = [input() for _ in range(N - 1)]


def build_cell_walls(v, h, N):
    """
    v[i][j] = マス(i,j)と(i,j+1)の間の壁 (長さN-1)
    h[i][j] = マス(i,j)と(i+1,j)の間の壁 (長さN)
    N = グリッドのサイズ (N×N)
    """
    cell_walls = [[{"U":False,"D":False,"L":False,"R":False} for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 左端・右端・上端・下端 → 枠外は壁とみなす
            if j == 0:
                cell_walls[i][j]["L"] = True
            if j == N-1:
                cell_walls[i][j]["R"] = True
            if i == 0:
                cell_walls[i][j]["U"] = True
            if i == N-1:
                cell_walls[i][j]["D"] = True

            # v: 左右の壁
            if j < N-1 and v[i][j] == '1':
                cell_walls[i][j]["R"] = True
                cell_walls[i][j+1]["L"] = True

            # h: 上下の壁
            if i < N-1 and h[i][j] == '1':
                cell_walls[i][j]["D"] = True
                cell_walls[i+1][j]["U"] = True

    return cell_walls

cell_walls = build_cell_walls(v, h, N)

from collections import deque

# 壁情報: walls[x][y] = {"U":bool, "D":bool, "L":bool, "R":bool}

def bfs_path(start, goal, walls, H, W):
    dirs = [(-1,0,"U"), (1,0,"D"), (0,-1,"L"), (0,1,"R")]
    rev = {"U":"D","D":"U","L":"R","R":"L"}
    dist = [[-1]*W for _ in range(H)]
    parent = {}
    move = {}
    q = deque([start])
    dist[start[0]][start[1]] = 0

    while q:
        x,y = q.popleft()
        if (x,y) == goal:
            break
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
        return None  # 行けない
    # 経路復元
    path = []
    cur = goal
    while cur != start:
        path.append(move[cur])
        cur = parent[cur]
    return path[::-1]


def sweep_all(H, W, walls, start=(0,0)):
    visited = [[False]*W for _ in range(H)]
    ops = []
    x,y = start
    visited[x][y] = True

    def all_visited():
        return all(all(row) for row in visited)

    while not all_visited():
        # 1. スネーク方向に進めるだけ進む
        moved = False
        for dx,dy,cmd in [(-1,0,"U"), (1,0,"D"), (0,-1,"L"), (0,1,"R")]:
            nx,ny = x+dx,y+dy
            if 0<=nx<H and 0<=ny<W:
                if not visited[nx][ny]:
                    if not walls[x][y][cmd] and not walls[nx][ny][{"U":"D","D":"U","L":"R","R":"L"}[cmd]]:
                        ops.append(cmd)
                        x,y = nx,ny
                        visited[x][y] = True
                        moved = True
                        break
        if moved:
            continue

        # 2. 未訪問セルを探す
        targets = [(i,j) for i in range(H) for j in range(W) if not visited[i][j]]
        if not targets:
            break
        # 近い未訪問セルを1つ選ぶ
        targets.sort(key=lambda t: abs(t[0]-x)+abs(t[1]-y))
        path = None
        for t in targets:
            path = bfs_path((x,y), t, walls, H, W)
            if path: 
                break
        if not path:
            break  # 行けない領域がある
        # BFS経路で移動
        for cmd in path:
            if cmd == "U": x-=1
            if cmd == "D": x+=1
            if cmd == "L": y-=1
            if cmd == "R": y+=1
            ops.append(cmd)
            visited[x][y] = True

    return "".join(ops)

c = [[None] * M for _ in range(K)]

c[0][0] = "U"
c[1][0] = "R"
c[2][0] = "D"
c[3][0] = "L"


for i in range(K):
    for j in range(M):
        if c[i][j] is None:
            c[i][j] = "U"
        
path = sweep_all(N, N, cell_walls, (0,0))

a = []
for p in path:
    if p == "U":
        a.append(0)
    elif p == "R":
        a.append(1)
    elif p == "D":
        a.append(2)
    elif p == "L":
        a.append(3)

for i in range(K):
    print(*c[i])

for button in a:
    print(button)


