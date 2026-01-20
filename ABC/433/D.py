from bisect import bisect_left, bisect_right
N, M = map(int, input().split())
A = list(map(int, input().split()))

as_mod = [[] for _ in range(11)]

for i in range(N):
    as_mod[len(str(A[i]))].append(A[i] % M)

for arr in as_mod:
    arr.sort()

ans = 0
ten = 10
for b in range(1, 11):
    for i in range(N):
        r = (-(A[i] * ten) % M)
        ans += bisect_right(as_mod[b], r) - bisect_left(as_mod[b], r)
    ten = (ten * 10) % M

print(ans)
# print(*as_mod[0])
