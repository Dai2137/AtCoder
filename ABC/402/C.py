N, M = map(int, input().split())
KAs = [list(map(int, input().split())) for _ in range(M)]
B = list(map(int, input().split()))

still = [KAs[i][0] for i in range(M)]

idxs = {}
for i in range(M):
    for j in range(1, KAs[i][0] + 1):
        if KAs[i][j] not in idxs:
            idxs[KAs[i][j]] = []
        idxs[KAs[i][j]].append(i)

ans = 0
for i in range(N):
    for j in idxs.get(B[i], []):  # ← ここを修正
        still[j] -= 1
        if still[j] == 0:
            ans += 1
    print(ans)
