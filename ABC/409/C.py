N, L = map(int, input().split())
d = list(map(int, input().split()))

if L % 3 != 0:
    print('0')
    exit()

S = [0] * N
for i in range(N - 1):
    S[i + 1] = S[i] + d[i]

cnt = [0] * L
for i in range(N):
    cnt[S[i] % L] += 1

ans = 0
for i in range(L//3):
    ans += cnt[i] * cnt[i + L//3] * cnt[i + 2 * L//3]

print(ans)
