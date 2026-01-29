N, M = map(int, input().split())
cnt = [N - 1] * N

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    cnt[A] -= 1
    cnt[B] -= 1
ans_l = []
for i in range(N):
    if cnt[i] < 2:
        ans = 0
    else:
        ans = cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
    ans_l.append(ans)
print(*ans_l)