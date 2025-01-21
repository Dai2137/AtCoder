from sortedcontainers import SortedList
N = int(input())
A = list(map(int,input().split()))

# D[i]->i人目の宇宙人が成人から石の数が0個になる~年後
D = [0] * N
D[0] = A[0] + 1
S = SortedList([D[0]])

for i in range(1, N):
    D[i] = i + 1 + A[i] + (len(S) - S.bisect_left(i + 1))
    S.add(D[i])
 
B = [None] * N 
for i in range(N):
    B[i] = max(0, D[i] - N)

print(*B)