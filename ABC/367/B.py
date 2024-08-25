X=list(input())
# print(X[0],X[1],X[2])
# i=0
# print(X[2]==X[3])
while X[-1]=="0":
  # print(X)
  X.pop()
  # print(X)
  # i+=1
  
if X[-1]==".":
  X.pop()
# print(X)
print("".join(X))