from bisect import bisect_left, bisect_right

N,Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

for _ in range(Q):k
  b, k = map(int,input().split())
  
  l= -1
  r = 2 * 10**8
  while l+1<r:
    M=(l+r)//2
    c = bisect_right(A,b+M) - bisect_left(A,b-M)
    if c>=k:
      r=M
    else:
      l=M
  print(r)

