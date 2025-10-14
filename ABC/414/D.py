N, M = map(int, input().split())
X = list(map(int, input().split()))

N = len(set(X))
P = max(0, N - M)

X = sorted(list(set(X)))

dist = []

for i in range(N - 1):
    dist.append(X[i + 1] - X[i])

dist.sort()

ans = sum(dist[:P])

print(ans)
# print(dist)
# print(P)

















