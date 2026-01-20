from atcoder.dsu import DSU

N, X, Y = map(int, input().split())
# rects: (lx, rx, ly, ry)
rects = [(0, X, 0, Y)]

for _ in range(N):
    C, A, B = input().split()
    A, B = int(A), int(B)
    old = rects.copy()
    rects = []

    if C == 'X':
        for lx, rx, ly, ry in old:
            if lx < A < rx:
                rects.append((lx, A, ly - B, ry - B))
                rects.append((A, rx, ly + B, ry + B))
            elif A <= lx:
                rects.append((lx, rx, ly + B, ry + B))
            else:
                rects.append((lx, rx, ly - B, ry - B))
                    
    else:
        for lx, rx, ly, ry in old:
            if ly < A < ry:
                rects.append((lx - B, rx - B, ly, A))
                rects.append((lx + B, rx + B, A, ry))
            elif A <= ly:
                rects.append((lx + B, rx + B, ly, ry))
            else:
                rects.append((lx - B, rx - B, ly, ry))

m = len(rects)
uf = DSU(m)

for i in range(m):
    lx1, rx1, ly1, ry1 = rects[i]
    for j in range(i):
        lx2, rx2, ly2, ry2 = rects[j]
        cx = min(rx1, rx2) - max(lx1, lx2)
        cy = min(ry1, ry2) - max(ly1, ly2)
        if cx < 0 or cy < 0:
            continue
        if cx != 0 or cy != 0:
            uf.merge(i, j)

areas = [0] * m
for i in range(m):
    lx, rx, ly, ry = rects[i]
    areas[uf.leader(i)] += (rx - lx) * (ry - ly)

areas.sort(reverse=True)
while areas and areas[-1] == 0:
    areas.pop()
areas.reverse()

print(len(areas))
print(*areas)
