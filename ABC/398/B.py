A = list(map(int, input().split()))

num = [0] * 14

for i in range(7):
    num[A[i]] += 1

num.sort()

if num[-1] >= 3 and num[-2] >= 2:
    print("Yes")
else:
    print("No")
