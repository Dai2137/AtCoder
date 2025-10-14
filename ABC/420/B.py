N, M = map(int, input().split())

point = [0] * N

S = [input() for _ in range(N)]

for i in range(M):
    x, y = 0, 0
    for j in range(N):
        if S[j][i] == '0':
            x += 1
        else:
            y += 1
    
    if x == 0 or y == 0:
        for j in range(N):
            point[j] += 1
    elif x < y:
        for j in range(N):
            if S[j][i] == '0':
                point[j] += 1
    else:
        for j in range(N):
            if S[j][i] == '1':
                point[j] += 1

max_point = max(point)
ans = []
for i in range(N):
    if point[i] == max_point:
        ans.append(i + 1)

print(*ans)
