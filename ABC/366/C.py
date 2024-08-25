# import bisect
# from collections import defaultdict
Q=int(input())
queries=[ input().split() for i in range(Q) ]
num={}


for q in queries:
  if q[0]=="1":
    if int(q[1]) not in num:
      num[int(q[1])]=1
    else:
      num[int(q[1])]+=1
    # S.append(q[1])
  elif q[0]=="2":
    num[int(q[1])]-=1
    if num[int(q[1])]==0:
      del num[int(q[1])]
    
  elif q[0]=="3":
    print(len(num))
  
