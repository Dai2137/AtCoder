N, K = map(int, input().split())
S = input()
ans = 0
count = 0
for i in range(N):
    if S[i] == 'X':
        ans += count // K
        count = 0
    elif S[i]=='O' and i!=N-1:
        count+=1
    else:
        count+=1
        ans += count // K
    # print(count)
print(ans)
