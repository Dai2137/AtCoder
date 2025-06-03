N, Q = map(int,input().split())

ans = 0
dict = {}
num_b = [1] * N

for i in range(N):
    dict[i] = i
    
for _ in range(Q):
    tph = list(map(int, input().split()))
    if len(tph) == 3:
        P, H = tph[1], tph[2]
        P -= 1
        H -= 1
        if num_b[dict[P]] == 2:
            ans -= 1
        if num_b[H] == 1:
            ans += 1
        num_b[dict[P]] -= 1
        num_b[H] += 1
        dict[P] = H
        
    else:
        print(ans)
        
        
    