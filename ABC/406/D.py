from sortedcontainers import SortedSet

H, W, N = map(int, input().split())
garbage = []
for _ in range(N):
    x, y = map(int, input().split())
    garbage.append((x - 1, y - 1))

Q = int(input())

garbage_num_x = [0] * H
garbage_num_y = [0] * W

for i in range(N):
    garbage_num_x[garbage[i][0]] += 1
    garbage_num_y[garbage[i][1]] += 1

garbage_x = [SortedSet() for _ in range(H)]
garbage_y = [SortedSet() for _ in range(W)]

for i in range(N):
    garbage_x[garbage[i][0]].add(garbage[i][1])
    garbage_y[garbage[i][1]].add(garbage[i][0])

already_x = [False] * H
already_y = [False] * W

for _ in range(Q):
    q, x = map(int, input().split())
    x -= 1
    if q == 1:
        if already_x[x]:
            print("0")
            continue
        print(garbage_num_x[x])
        for gx in garbage_x[x]:
            garbage_y[gx].discard(x)
            garbage_num_y[gx] -= 1
        
        # garbage_x[x] = SortedSet()
        already_x[x] = True
        
    else:
        y = x
        if already_y[y]:
            print("0")
            continue
        print(garbage_num_y[y])
        for gy in garbage_y[y]:
            garbage_x[gy].discard(y)
            garbage_num_x[gy] -= 1
        # garbage_y[y] = SortedSet()
        already_y[y] = True
