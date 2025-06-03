# 移動と滑走のみでの最適解を求める
# ある目的マスから次の目的マスへ移動する際、「滑走」は高々2 回しか使わないので、これを全探索して解を求める。

def move_to(nowi, nowj, targeti, targetj, action, t, limit):
    while nowi < targeti and t <= limit:
        action.append(('M', 'D'))  # 縦に下がる = D
        nowi += 1
        t += 1
    while nowi > targeti and t <= limit:
        action.append(('M', 'U'))  # 縦に上がる = U
        nowi -= 1
        t += 1
    while nowj < targetj and t <= limit:
        action.append(('M', 'R'))  # 横に右 = R
        nowj += 1
        t += 1
    while nowj > targetj and t <= limit:
        action.append(('M', 'L'))  # 横に左 = L
        nowj -= 1
        t += 1
    return nowi, nowj, t

N, M = map(int, input().split())
target = [tuple(map(int, input().split())) for _ in range(M)]

action = []
t = 0
nowi, nowj = target[0][0], target[0][1]
limit = 2 * N * M

# 最初のターゲットへ
# nowi, nowj, t = move_to(nowi, nowj, target[0][0], target[0][1], action, t, limit)

for idx in range(M-1):
    nowi, nowj, t = move_to(nowi, nowj, target[idx+1][0], target[idx+1][1], action, t, limit)

for a, d in action:
    print(a, d)
