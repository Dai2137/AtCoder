S = list(input())

s = 0
# print(S)
for i in range(len(S) - 1, -1, -1):
    S[i] = int(S[i])
    S[i] = (S[i] - s) % 10
    s += S[i]
    # print(s)

s += len(S)
print(s)


