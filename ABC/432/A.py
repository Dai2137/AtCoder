A, B, C = map(int, input().split())

A = [A, B, C]

A.sort(reverse=True)

print(A[0] * 100 + A[1] * 10 + A[2])
