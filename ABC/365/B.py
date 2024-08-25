N=int(input())
A=list(map(int,input().split()))

# B=A.copy()
# A.sort()
# for i in range(N):
#   if B[i]==A[-2]:
#     print(i+1)
#     exit()

# 模範解答
print(A.index(sorted(A)[-2]+1))