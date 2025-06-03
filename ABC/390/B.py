N = int(input())
A = list(map(int, input().split()))

# S = set([])
# a = A[1] / A[0]
flag = True
for i in range(N-2):
    if A[i+1] ** 2 != A[i] * A[i+2]:
        flag = False
print("Yes" if flag else "No")