N = int(input())
A = list(map(int, input().split()))

B = [None] * N

address = {}
for i in range(N):
    if A[i] not in address:
        B[i] = -1
        address[A[i]] = [i]
    else:
        B[i] = address[A[i]][-1] + 1
        address[A[i]].append(i)
print(*B)