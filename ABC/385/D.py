from sortedcontainers import SortedList
N, M, Sx, Sy = map(int, input().split())

hx = {}
hy = {}

for _ in range(N):
    X, Y = map(int, input().split())
    if X not in hx:
        hx[X] = SortedList()
    hx[X].add(Y)

    if Y not in hy:
        hy[Y] = SortedList()
    hy[Y].add(X)

cnt = 0
for _ in range(M):
    D, C = input().split()
    C = int(C)

    if D == 'U':
        slist = hx.get(Sx, SortedList())  # KeyError 防止
        if slist:
            r = slist.bisect_right(Sy + C) - 1
            l = slist.bisect_left(Sy)

            # 境界チェック
            if 0 <= l <= r < len(slist):
                cnth = r - l + 1
                for yi in list(slist.irange(Sy, Sy + C)):  # 削除前にリスト化
                    slist.discard(yi)
                    if yi in hy and Sx in hy[yi]:
                        hy[yi].discard(Sx)
            else:
                cnth = 0
        else:
            cnth = 0

        cnt += cnth
        Sy += C

    elif D == 'D':
        slist = hx.get(Sx, SortedList())  # KeyError 防止
        if slist:
            r = slist.bisect_right(Sy) - 1
            l = slist.bisect_left(Sy - C)

            # 境界チェック
            if 0 <= l <= r < len(slist):
                cnth = r - l + 1
                for yi in list(slist.irange(Sy - C, Sy)):
                    slist.discard(yi)
                    if yi in hy and Sx in hy[yi]:
                        hy[yi].discard(Sx)
            else:
                cnth = 0
        else:
            cnth = 0

        cnt += cnth
        Sy -= C

    elif D == 'L':
        slist = hy.get(Sy, SortedList())  # KeyError 防止
        if slist:
            r = slist.bisect_right(Sx) - 1
            l = slist.bisect_left(Sx - C)

            if 0 <= l <= r < len(slist):
                cnth = r - l + 1
                for xi in list(slist.irange(Sx - C, Sx)):
                    slist.discard(xi)
                    if xi in hx and Sy in hx[xi]:
                        hx[xi].discard(Sy)
            else:
                cnth = 0
        else:
            cnth = 0

        cnt += cnth
        Sx -= C

    elif D == 'R':
        slist = hy.get(Sy, SortedList())  # KeyError 防止
        if slist:
            r = slist.bisect_right(Sx + C) - 1
            l = slist.bisect_left(Sx)

            if 0 <= l <= r < len(slist):
                cnth = r - l + 1
                for xi in list(slist.irange(Sx, Sx + C)):
                    slist.discard(xi)
                    if xi in hx and Sy in hx[xi]:
                        hx[xi].discard(Sy)
            else:
                cnth = 0
        else:
            cnth = 0

        cnt += cnth
        Sx += C

print(Sx, Sy, cnt)
