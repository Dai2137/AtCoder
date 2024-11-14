N,M  = map(int,input().split())
birthed = [False]* N

for _ in range(M):
  A,B = input().split()
  A = int(A)
  if B == "F":
    print("No")
    continue
  if birthed[A-1]:
    print("No")
    continue
  else:
    print("Yes")
    birthed[A-1] = True
