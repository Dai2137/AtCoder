N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

if S[N] - S[N- K] < X:
    print(-1)
    exit()

ok = N
ng = 0

def judge(n):
    if S[n] - S[N - K] >= X:
        return True
    else:
        return False


while ng + 1 < ok:
    mid = (ng + ok) // 2
    if judge(mid):
        ok = mid
    else:
        ng = mid

print(ok)