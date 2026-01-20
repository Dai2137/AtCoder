N = int(input())

T = list(map(int, input().split()))

T_sorted = sorted(T)

for i in range(N):
    if T[i] == T_sorted[0]:
        top1 = i + 1
    if T[i] == T_sorted[1]:
        top2 = i + 1
    if T[i] == T_sorted[2]:
        top3 = i + 1

print(top1, top2, top3)