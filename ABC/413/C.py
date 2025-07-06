from collections import deque

Q = int(input())

A = deque()
for _ in range(Q):
    Ns = list(map(int, input().split()))
    
    if Ns[0] == 1:
        c, x = Ns[1], Ns[2]
        A.append((x, c))
    else:
        k = Ns[1]
        ans = 0
        while k > 0:
            num = min(k, A[0][1])
            ans += A[0][0] * num
            if k < A[0][1]:
                A[0] = (A[0][0], A[0][1] - k)
                break
            else:
                k -= A[0][1]
                A.popleft()
                
        print(ans)

            
        
