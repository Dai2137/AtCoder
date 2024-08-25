N=int(input())

# # 全探索 O(N)
# for i in range(1, 1000004):
#   if int(str(i)*2)>N:
#     print(i-1)
#     exit()

# 二分探索 O(logN)
L,R=0,1000004
while R-L>1:
  M=(L+R)//2
  if int(str(M)*2)>N:
    R=M
  else:
    L=M
print(L)