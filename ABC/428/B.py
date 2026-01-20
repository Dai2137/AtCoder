N, K = map(int, input().split())

S = input()


dict = {}

for i in range(N - K + 1):
    t = S[i:i+K]
    if t not in dict:
        dict[t] = 0
    dict[t] += 1

ans_list = []
x = -1

for k, v in dict.items():
    if v > x:
        x = v

for k, v in dict.items():
    if v == x:
        ans_list.append(k)
print(x)
ans_list.sort()
print(*ans_list)
