N = int(input())
S = input()

l = []

for i in range(N):
    if S[i]=='1':
        l.append(i)

n = len(l)
ans = 0


m = n // 2
for i in range(n):
    ans += abs(l[i] - (l[m] - m + i))

print(ans)


# if n % 2 == 1:
#     m = (n - 1) // 2
#     for i in range(n):
#         ans += abs(l[i] - (l[m] - m + i))

# else:
#     m = n // 2
    
        