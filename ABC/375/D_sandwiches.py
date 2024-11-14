from collections import defaultdict
S = input()

d = defaultdict()

for i in range(len(S)):
    if S[i] not in d:
        d[S[i]] = []
    d[S[i]].append(i)

ans = 0
for key in d.keys():
    for i in range(len(d[key]) - 1):
    #   for j in range(i + 1, len(d[key])):
    #     ans += d[key][j] - d[key][i] - 1
        ans += (i+1) * (len(d[key]) - i - 1) * (d[key][i+1] - d[key][i])
    ans -= len(d[key]) * (len(d[key]) - 1) // 2
    # print(ans)

print(ans)

