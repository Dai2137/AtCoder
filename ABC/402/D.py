N, M = map(int, input().split())
ans = M * (M - 1) // 2
mod = [0] * N
for i in range(M):
    A, B = map(int, input().split())
    mod[(A + B) % N] += 1

for i in range(N):
    ans -= mod[i] * (mod[i] - 1) // 2
print(ans)