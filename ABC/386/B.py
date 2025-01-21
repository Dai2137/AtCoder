S = input()
ans = len(S)
list = []
cnt = 0
for i in range(len(S)):
    if S[i]=="0":
        cnt+=1
        if i == len(S) - 1:
            list.append(cnt)
    elif i > 0 and S[i] != "0" and S[i - 1] == "0":
        list.append(cnt)
        cnt = 0

for i in list:
    ans -= i//2
print(ans)