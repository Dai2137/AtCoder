from itertools import combinations
N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
ans = M + 2
for i in range(N // 2 + 1):
    for v in combinations(range(N), i):
        m = 0
        # n_kanzen = i * (N - i)
        rest = tuple(set(range(N)) - set(v))
        for j in v:
            for k in rest:
                if k in G[j]:
                    m += 1
        l = M - m
        ans = min(ans, l)

print(ans)