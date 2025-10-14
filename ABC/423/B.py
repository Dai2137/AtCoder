N = int(input())
L = list(map(int, input().split()))

one_min = 10**10
one_max = -1

for i in range(N):
    if L[i] == 1:
        if one_min > i:
            one_min = i
        if one_max < i:
            one_max = i

if one_min == 10**10:
    print(0)
else:
    print(one_max - one_min)

