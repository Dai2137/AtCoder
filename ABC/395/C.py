N = int(input())
A = list(map(int, input().split()))

if len(A) == len(set(A)):
    print(-1)
    exit()

dict = {}

for i in range(N):
    if A[i] not in dict:
        dict[A[i]] = []
    dict[A[i]].append(i)

ans = 10 ** 10
for i in dict:
    for j in range(len(dict[i]) - 1):
        ans = min(ans, dict[i][j + 1] - dict[i][j] + 1)

print(ans)