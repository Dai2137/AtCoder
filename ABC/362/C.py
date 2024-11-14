N = int(input())
L, R = [], []
for _ in range(N):
    Li, Ri = map(int,input().split())
    L.append(Li)
    R.append(Ri)

if 0 < sum(L) or sum(R) < 0:
    print("No")
    exit()

X = []
for i in range(N):
    X.append(L[i])

notyetplus = - sum(L)
# print(notyetplus)
for i in range(N):
    if notyetplus > R[i] - L[i]:
        X[i] = R[i]
        # print(X[i],R[i],L[i])
        notyetplus -= R[i] - L[i]
        # print(notyetplus)
    elif notyetplus == R[i] - L[i]:
        X[i] = R[i]
        break
    else:
        X[i] += notyetplus
        break

print("Yes")
print(*X)