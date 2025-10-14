N, R = map(int, input().split())
L = list(map(int, input().split()))
ans = 0

zero_min = 10**10
zero_max = -1

for i in range(N):
    if L[i] == 0:
        if zero_min > i:
            zero_min = i
        if zero_max < i:
            zero_max = i


for i in range(N):
    if L[i] == 0:
        ans += 1
    elif L[i] == 1 and R <= i and zero_max < i:
        continue
    elif L[i] == 1 and i < R and i < zero_min:
        continue
    else:
        ans += 2
        
print(ans)
