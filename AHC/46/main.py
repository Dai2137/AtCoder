# ======================
# 必要な関数定義
# ======================

from collections import deque

def try_place_or_remove_block(nowi, nowj, action, t, limit, block_idxs, should_place_block):
    """今いる位置の上下左右にブロックを置いたり除去したりする"""
    for di, dj, dir_char in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
        ni, nj = nowi + di, nowj + dj
        if 0 <= ni < N and 0 <= nj < N and t <= limit:
            if (ni, nj) in should_place_block and (ni, nj) not in block_idxs:
                action.append(('A', dir_char))  # ブロックを置く
                block_idxs.append((ni, nj))
                t += 1
            elif (ni, nj) in block_idxs and (ni, nj) not in should_place_block:
                action.append(('A', dir_char))  # ブロックを除去する
                block_idxs.remove((ni, nj))
                t += 1
    return t

def bfs(nowi, nowj, targeti, targetj, block_idxs):
    """BFSで最短ルート探索"""
    q = deque()
    q.append((nowi, nowj))
    prev = dict()
    visited = set()
    visited.add((nowi, nowj))

    while q:
        i, j = q.popleft()
        if (i, j) == (targeti, targetj):
            break
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if (ni, nj) not in block_idxs and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    prev[(ni, nj)] = (i, j)
                    q.append((ni, nj))

    path = []
    cur = (targeti, targetj)
    while cur != (nowi, nowj):
        path.append(cur)
        if cur in prev:
            cur = prev[cur]
        else:
            return []
    path.reverse()
    return path

def try_slide(nowi, nowj, targeti, targetj, block_idxs, action, t, limit):
    """滑走できるならする"""
    if nowi != targeti:
        return nowi, nowj, t, False

    # 右に滑走
    if nowj < targetj and (targeti, targetj-1) in block_idxs and (targeti, targetj+1) in block_idxs:
        while nowj + 1 < N and (nowi, nowj + 1) not in block_idxs:
            action.append(('S', 'R'))
            nowj += 1
            t += 1
            if (nowi, nowj) == (targeti, targetj):
                return nowi, nowj, t, True
    # 左に滑走
    elif nowj > targetj and (targeti, targetj-1) in block_idxs and (targeti, targetj+1) in block_idxs:
        while nowj - 1 >= 0 and (nowi, nowj - 1) not in block_idxs:
            action.append(('S', 'L'))
            nowj -= 1
            t += 1
            if (nowi, nowj) == (targeti, targetj):
                return nowi, nowj, t, True

    return nowi, nowj, t, False

def move_to(nowi, nowj, targeti, targetj, action, t, limit, block_idxs, should_place_block):
    """ターゲットに向かう、滑走・ブロック設置除去すべてあり"""
    while (nowi, nowj) != (targeti, targetj) and t <= limit:
        t = try_place_or_remove_block(nowi, nowj, action, t, limit, block_idxs, should_place_block)

        # 滑走を優先的に試す
        nowi, nowj, t, slid = try_slide(nowi, nowj, targeti, targetj, block_idxs, action, t, limit)
        if slid:
            return nowi, nowj, t

        # 滑走できなければBFSで道を探す
        path = bfs(nowi, nowj, targeti, targetj, block_idxs)
        if not path:
            # パスがなかったらブロックを除去して次ターン
            t = try_place_or_remove_block(nowi, nowj, action, t, limit, block_idxs, should_place_block)
            continue

        # 次の1マスだけ進む
        nexti, nextj = path[0]

        if nexti == nowi + 1 and nextj == nowj:
            action.append(('M', 'D'))
        elif nexti == nowi - 1 and nextj == nowj:
            action.append(('M', 'U'))
        elif nexti == nowi and nextj == nowj + 1:
            action.append(('M', 'R'))
        elif nexti == nowi and nextj == nowj - 1:
            action.append(('M', 'L'))

        nowi, nowj = nexti, nextj
        t += 1

    return nowi, nowj, t





# 入力
N, M = map(int, input().split())
target = [tuple(map(int, input().split())) for _ in range(M)]

# ブロックを置くべきマス（左右にブロックを置く）
should_place_block = []
for i in range(1, M):
    if target[i][1] < target[i - 1][1] and target[i][1] - 1 >= 0:
        should_place_block.append((target[i][0], target[i][1] - 1))
    elif target[i][1] > target[i - 1][1] and target[i][1] + 1 < N:
        should_place_block.append((target[i][0], target[i][1] + 1))

# ======================
# 実行
# ======================
action = []
t = 0
block_idxs = []
limit = 2 * N * M
nowi, nowj = target[0]

for idx in range(1, M):
    nowi, nowj, t = move_to(nowi, nowj, target[idx][0], target[idx][1], action, t, limit, block_idxs, should_place_block)

for a, d in action:
    print(a, d)