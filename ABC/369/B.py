N = int(input())
L = []
R = []

for _ in range(N):
  A, S = input().split()
  A=int(A)
  if S=='L':
    L.append(A)
  else:
    R.append(A)

ans = 0
for i in range(len(L)-1):
  ans+=abs(L[i+1]-L[i])

for i in range(len(R)-1):
  ans+=abs(R[i+1]-R[i])

print(ans)