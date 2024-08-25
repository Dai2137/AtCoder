H,W=map(int,input().split())
Si,Sj=map(int,input().split())
C=[input() for _ in range(H)]
X=input()

Si, Sj = Si-1, Sj-1

for i in range(len(X)):
    if X[i]=="R" and Sj<W-1 and C[Si][Sj+1]==".":
        Sj+=1
    elif X[i]=="L" and Sj>0 and C[Si][Sj-1]==".":
        Sj-=1
    elif X[i]=="D" and Si<H-1 and C[Si+1][Sj]==".":
        Si+=1
    elif X[i]=="U" and Si>0 and C[Si-1][Sj]==".":
        Si-=1

print(Si+1, Sj+1)
# print(C[Si+1][Sj+1])