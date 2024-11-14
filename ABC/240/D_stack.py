N=int(input())
a=list(map(int,input().split()))

queue = []
count = []
ans = 0

for i in range(N):
  queue.append(a[i])
  ans+=1
  
  if len(queue) >= 2 and queue[-1]==queue[-2]:
    count[-1]+=1
    if count[-1]==queue[-1]:
      temp = queue[-1]
      for i in range(queue[-1]):
        queue.pop()
      ans-=temp
      count.pop()
  
  else:
    count.append(1)
  
  print(ans)