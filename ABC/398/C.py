N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(1)
    exit()
if N == 2:
    if A[0] == A[1]:
        print(-1)
    elif A[0] < A[1]:
        print(2)
    else:
        print(1)
    exit()
    
         



B = A.copy()

A.sort()


# val = -1
ans = -1
for i in range(N - 1, -1, -1):
    if i == N - 1 and A[i] != A[i - 1]:
        ans = A[i]
        break
    elif 0 < i < N - 1 and A[i] != A[i + 1] and A[i] != A[i - 1]:
        ans = A[i]
        break
    elif i == 0 and A[i] != A[i + 1]:
        ans = A[i]
        break

for i in range(N):
    if B[i] == ans:
        ansa = i + 1

if ans == -1:
    ansa = -1

print(ansa)
    
    
        
    
    
