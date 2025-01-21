Q = int(input())
# 累積和
S = [0]
cnt_2 = 0

for q in range(Q):
    temp = list(map(int, input().split()))
    if temp[0]==1:
        l = temp[1]
        temp2 = S[-1]
        S.append(temp2 + l)
    elif temp[0]==2:
        cnt_2 += 1
    else:
        k = temp[1] - 1
        print(S[k + cnt_2] - S[cnt_2])

