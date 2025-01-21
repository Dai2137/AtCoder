X = int(input())
ans = 2025
for i in range(1,10):
    for j in range(1,10):
        if i*j==X:
            ans -= X

print(ans)