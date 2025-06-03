N, M = map(int, input().split())

S = [0] * (N + 1)

for _ in range(M):
    l, r = map(int, input().split())
    S[l - 1] += 1
    S[r] -= 1

for i in range(N):
    S[i + 1] += S[i]
S.pop()
print(min(S))
