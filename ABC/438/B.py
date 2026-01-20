N, M = map(int, input().split())

S = input()
T = input()

ans = 10 ** 18

for i in range(N - M + 1):
    s = S[i:i+M]
    cnt = 0
    for j in range(M):
        if T[j] < s[j]:
            cnt += int(s[j]) - int(T[j])
        elif T[j] > s[j]:
            cnt += int(s[j]) - int(T[j]) + 10
    ans = min(ans, cnt)
    # print(s, cnt)
print(ans)