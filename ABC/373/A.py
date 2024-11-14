ans = 0
for i in range(12):
    ans += len(input()) == i + 1
print(ans)