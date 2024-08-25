N=int(input())

S=[None]*N
for i in range(N):
    S[i]=input()

ans=True

for i in range(N-2):
    if S[i]=="sweet" and S[i+1]=="sweet":
        ans=False
        break

if ans:
    print("Yes")
else:
    print("No")