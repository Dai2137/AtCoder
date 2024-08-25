N,X,Y=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

# Aで大きいものから食べていく
A.sort(reverse=True)
A_eat=0
for i in range(N):
  A_eat+=A[i]
  if A_eat>X or i==N-1:
    A_num = i+1
    break
    

# Bで大きいものから食べていく
B.sort(reverse=True)
B_eat=0
for i in range(N):
  B_eat+=B[i]
  if B_eat>Y or i==N-1:
    B_num = i+1
    break

ans=min(A_num,B_num)
print(ans)
