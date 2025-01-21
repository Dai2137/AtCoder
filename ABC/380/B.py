S = input()
A = []

count = 0
for i in range(1, len(S)):
    if S[i]=='-':
        count += 1 
    else:
        A.append(count)
        count = 0
print(*A)