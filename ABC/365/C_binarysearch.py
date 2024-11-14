def score(A,x):
  return sum(min(a,x) for a in A)

N,M=map(int,input().split())
A=list(map(int,input().split()))

if sum(A)<=M:
  print("infinite")
  exit()


ok,ng=0,10**14+1
while ng-ok>1:
  mid=(ok+ng)//2
  if score(A,mid)<=M:
    ok=mid
  else:
    ng=mid
print(ok)