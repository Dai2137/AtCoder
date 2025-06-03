N, M = map(int, input().split())
A = []
# 上限のやつ
dp = {}

def dfs(n: int, l: int):
    if (n, l) in dp:
        return dp[(n, l)]
    B = []
    if n > M:
        return
    # print(n)
    if l == 1:
        return [[n]]
    for i in range(n + 10, M + 1):
        C = dfs(i, l - 1).copy()
        # print(C)
        for c in C:
            # print(c)
            B.append([n] + c)
    dp[(n, l)] = B.copy()
    return B.copy()

for i in range(1, M - 10 * (N - 1) + 1):
    C = dfs(i, N).copy()
    # print(1)
    
    for c in C:
        A.append(c)

# print(dfs(24, N))

print(len(A))
for a in A:
    print(*a)

# print(A)