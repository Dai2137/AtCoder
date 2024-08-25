N=int(input())
A=list(map(int,input().split()))
ans=0
while sum(1 for a in A if a>0)>1:
  A.sort(reverse=True)
  A[0]-=1
  A[1]-=1
  ans+=1
print(ans)