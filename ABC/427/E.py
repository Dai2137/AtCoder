from collections import deque
H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == "T":
            ti, tj = i, j

dist = {}
que = deque()

# li, ri, lj, rj, dti, dtj
dist[(0, H-1, 0, W-1, 0, 0)] = 0
que.append((0, H-1, 0, W-1, 0, 0))


def push(li, ri, lj, rj, ni, nj, d):
    li = max(li, ni)
    ri = min(ri, ni + H - 1)
    lj = max(lj, nj)
    rj = min(rj, nj + W - 1)
    
    if li <= ti + ni <= ri and lj <= tj + nj <= rj and S[ti + ni][tj + nj] == "#":
        return
    
    if (li, ri, lj, rj, ni, nj) in dist:
        return
    dist[(li, ri, lj, rj, ni, nj)] = d
    que.append((li, ri, lj, rj, ni, nj))

while que:
    li, ri, lj, rj, dti, dtj = que.popleft()
    num_gomi = 0
    for i in range(li, ri + 1):
        for j in range(lj, rj + 1):
            if S[i][j] == "#":
                num_gomi += 1
    if num_gomi == 0:
        print(dist[(li, ri, lj, rj, dti, dtj)])
        exit()
    d = dist[(li, ri, lj, rj, dti, dtj)]
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = dti + di, dtj + dj
        push(li, ri, lj, rj, ni, nj, d + 1)
print(-1)
