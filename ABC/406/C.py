N = int(input())
P = list(map(int, input().split()))

valley = []
mountain = []

for i in range(N):
    if i == 0:
        if P[i] < P[i + 1]:
            valley.append(i)
    elif i == N - 1:
        if P[i - 1] < P[i]:
            mountain.append(i)
    else:
        if P[i - 1] < P[i] and P[i] > P[i + 1]:
            mountain.append(i)
        elif P[i - 1] > P[i] and P[i] < P[i + 1]:
            valley.append(i)

nv = len(valley)
nm = len(mountain)

ans = 0

for i in range(nv):
    if i + 1 < nv:
        ans += (mountain[i] - valley[i]) * (mountain[i + 1] - valley[i + 1])

print(ans)
