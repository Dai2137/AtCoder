S = list(input())

N = len(S)
cnt = 0
L = []
flg = False
for i in range(N):
    if S[i] == 'W':
        if not flg:
            idx = i
        flg = True
        cnt += 1
        
    elif S[i] == 'A':
        if flg:
            L.append((idx, cnt))
            flg = False
            cnt = 0
    else:
        flg = False
        cnt = 0
        

for j in range(len(L)):
    S[L[j][0]: L[j][0] + L[j][1] + 1] = 'A' + 'C' * L[j][1]

print("".join(S))
            