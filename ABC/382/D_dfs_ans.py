N, M = map(int, input().split())
ans = []
def dfs(v):
    sz = len(v)
    if sz == N:
        ans.append(v)
        return
    start = 1 if sz == 0 else v[-1] + 10
    end = M - 10 * (N - sz - 1)
    for i in range(start, end + 1):
        dfs(v + [i])

dfs([])

print(len(ans))
for a in ans:
    print(*a)
