N, S = map(int, input().split())
T = list(map(int, input().split()))

A = [T[0]]

for i in range(1, N):
    A.append(T[i] - T[i-1])
if max(A) > S:
    print("No")
else:
    print("Yes")

