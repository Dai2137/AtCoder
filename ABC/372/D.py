N = int(input())
H = list(map(int,input().split()))

s = []
ans = [None] * N
ans[N-1] = 0

for i in range(N-2, -1, -1):
    while s and s[-1] < H[i+1]:
        s.pop()
    s.append(H[i+1])
    ans[i] = len(s)
print(*ans)
