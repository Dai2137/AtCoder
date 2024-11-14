from sortedcontainers import SortedList

H, W, Q = map(int, input().split())

row = [SortedList(range(W)) for _ in range(H)]
col = [SortedList(range(H)) for _ in range(W)]

for _ in range(Q):
    R, C = map(lambda x: int(x) - 1, input().split())

    pos = row[R].bisect_left(C)
    if pos < len(row[R]) and row[R][pos] == C:
        row[R].remove(C)
        col[C].remove(R)
        continue
    if pos < len(row[R]):
        val = row[R][pos]
        row[R].remove(val)
        col[val].remove(R)
    if pos > 0:
        val = row[R][pos - 1]
        row[R].remove(val)
        col[val].remove(R)

    pos = col[C].bisect_left(R)
    if pos < len(col[C]):
        val = col[C][pos]
        row[val].remove(C)
        col[C].remove(val)
    if pos > 0:
        val = col[C][pos - 1]
        row[val].remove(C)
        col[C].remove(val)

print(sum(len(r) for r in row))
