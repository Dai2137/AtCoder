A = list(map(int, input().split()))
ans=0
num = [0] * 4
for i in range(4):
    num[A[i] - 1] += 1
for i in range(4):
    ans += num[i] // 2
print(ans)