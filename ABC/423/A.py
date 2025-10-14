X, C = map(int, input().split())
ans = 0
for i in range(10 ** 5):
    hikidashi = i * 1000
    siharai = hikidashi + hikidashi * C // 1000
    if siharai <= X:
        ans = hikidashi
    else:
        break

print(ans)
