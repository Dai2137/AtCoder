from collections import deque
H, W = map(int ,input().split())

S = [list(input()) for _ in range(H)]

didj = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
ans = 0
used = [[False] * W for i in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            ans += 1
            que = deque([(i, j)])
            while que:
                sensori, sensorj =  que.popleft()
                # S[sensori][sensorj] = '.'
                for di, dj in didj:
                    sensoridi = sensori + di
                    sensorjdj = sensorj + dj
                    if 0 <= sensoridi < H and 0 <= sensorjdj < W and S[sensoridi][sensorjdj] == '#':
                        # used[sensoridi][sensorjdj] = True
                        S[sensoridi][sensorjdj] = '.'
                        que.append((sensoridi, sensorjdj))

print(ans)