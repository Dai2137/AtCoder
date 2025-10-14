S = input()
N = len(S)
ans = 0.0
for L in range(N):
    for R in range(L, N):
        t = S[L:R+1]
        if len(t) >= 3 and t[0] == t[-1] == 't':
            x = t.count('t')
            ans = max(ans, (x - 2) / (len(t) - 2))
print(ans)
