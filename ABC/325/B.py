N = int(input())
W , X = [], []

for i in range(N):
    Wi, Xi = map(int, input().split())
    W.append(Wi)
    X.append(Xi)

ans = -1
for i in range(24):
    temp = 0
    for j in range(N):
        if 9 <= (i + X[j]) <= 17 or 33 <= (i + X[j]) <= 41:
            temp += W[j]
    ans = max(temp, ans)

print(ans)