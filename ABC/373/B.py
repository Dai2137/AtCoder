S = input()
dic = {}
for i in range(26):
    dic[S[i]] = i

ans = 0
for i in range(25):
    ans += abs(dic[chr(ord('A') + i + 1)] - dic[chr(ord('A') + i)])

print(ans)