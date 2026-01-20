T = int(input())

def solve():
    N, W = map(int, input().split())
    C = list(map(int, input().split()))
    w2 = 2 * W
    D = [0] * w2
    for i in range(N):
        D[i % w2] += C[i]
    D = D + D
    
    window = sum(D[:W])
    ans = window
    for s in range(1, w2):
        window += D[s - 1 + W] - D[s - 1]
        if window < ans:
            ans = window
    print(ans)
    
    
    
    
    
    
    
    
    
    
    
    # m = 2 * W
    # A = [0] * m
    
    # for i in range(1, N + 1):
    #     A[ i % m] += C[i - 1]
    
    # A2 = A + A
    # window = sum(A2[:W])
    # ans = window
    # for s in range(1, m):
    #     window += A2[s + W - 1] - A2[s - 1]
    #     if window < ans:
    #         ans = window
    # print(ans)
    
for _ in range(T):
    solve()