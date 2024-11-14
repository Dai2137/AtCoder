from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))

def combination2(N):
  return (N*(N-1))//2

D = [A[i+1]-A[i] for i in range(N-1)]

ct = defaultdict(int)
s=1
for i in range(N-1):
  if i==N-2:
    ct[s+1]+=1
  elif D[i+1]!=D[i]:
    ct[s+1]+=1
    s=1
  else:
    s+=1


ans=0
for key, value in ct.items():
  ans+=combination2(key)*value
ans+=N
print(ans)
# print(ct)