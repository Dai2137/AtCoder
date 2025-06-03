N = int(input())

ord = []

ans = ""
S = []
for i in range(N):
    s = input()
    S.append(( len(s) ,i, s))

S.sort()

for i in range(N):
    ans += S[i][2]

print(ans) 