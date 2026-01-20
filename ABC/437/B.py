H, W, N = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]
B = []
for i in range(N):
    B.append(int(input()))

ans = 0

for i in range(H):
    cnt = 0
    for j in range(W):
        if A[i][j] in B:
            cnt += 1
    ans = max(ans, cnt)
print(ans)