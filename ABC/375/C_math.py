import copy
N = int(input())
A = [list(input()) for row in range(N)]

# B = [[None] * N for row in range(N)]
B = copy.deepcopy(A)
for i in range(1, N//2 + 1):
    for x in range(i, N + 1 - i + 1):
        for y in range(i, N + 1 - i + 1):
            B[y - 1][N + 1 - x - 1] = A[x - 1][y - 1]
            # if i==1 and x==1 and y ==8:
            #     print(A)
            #     print(B)
            # if i==1:
            #   print(y)
    # if i == 1:
    #   print(B)
    A = copy.deepcopy(B)

for i in range(N):
    print("".join(B[i]))
# print(B)