N, M = map(int, input().split())
S = input()
T = input()

cnt = [0] * (N + 1)

for i in range(M):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1
    cnt[l] += 1
    cnt[r + 1] -= 1

for i in range(N):
    cnt[i + 1] += cnt[i]

S_ans = []
for i in range(N):
    if cnt[i] % 2 == 0:
        S_ans.append(S[i])
    else:
        S_ans.append(T[i])

print("".join(S_ans))
