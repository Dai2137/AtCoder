S = input()

ans = 0
N = len(S)
for i in range(N-2):
    for j in range(i+1,N-1):
        k = 2 * j - i
        if k < N and S[i] == 'A' and S[j] == 'B' and S[k] == 'C':
            ans += 1

print(ans)