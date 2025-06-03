S = input()
N = len(S)
cnt = 0
for i in range(N - 1):
    if S[i:i + 2] == "io":
        cnt += 1

print(N - 2 * cnt)