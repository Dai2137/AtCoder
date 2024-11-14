N = int(input())
K = list(map(int,input().split()))

ans = 10 ** 10
S = sum(K)

for i in range(2 ** N):
    group = 0
    for j in range(N):
        if ((i >> j) & 1):
            group += K[N - 1 - j]
    maxgroup = max(group, S - group)
    ans = min(ans, maxgroup)

print(ans) 