N = int(input())
S = input()

ans = 0
for i in range(N - 2):
    ans += (S[i]=="#" and S[i+1]=="." and S[i+2]=="#")
    # if (S[i]=="#" and S[i+1]=="." and S[i+2]=="#"):
    #     print(i)

print(ans)