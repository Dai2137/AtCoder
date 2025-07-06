N, Q = map(int, input().split())
X = list(map(int, input().split()))

B = []
box = [0] * N

for i in range(Q):
    if X[i] >= 1:
        box[X[i] - 1] += 1
        B.append(X[i])
    else:
        ans = 10000
        temp = -1
        for j in range(N):
            if box[j] < ans:
                temp = j
                ans = box[j]
        box[temp] += 1
        B.append(temp + 1)
print(*B)

