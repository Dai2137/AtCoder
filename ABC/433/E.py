T = int(input())

def solve():
    H, W = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    
    rid, cid = {}, {}
    for i in range(H):
        rid[X[i]] = i
    for j in range(W):
        cid[Y[j]] = j
    
    X.sort(reverse=True)
    Y.sort(reverse=True)
    
    a = [[0] * W for _ in range(H)]
    
    xi, yi = 0, 0
    cand = []
    
    for v in range(H * W, 0, -1):
        if xi < H and X[xi] == v:
            for j in range(yi):
                cand.append((xi, j))
            xi += 1
        
        if yi < W and Y[yi] == v:
            for i in range(xi):
                cand.append((i, yi))
            yi += 1
        
        if not cand:
            print("No")
            return
        
        i, j = cand.pop()
        a[i][j] = v
        
    
    ans = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            ans[rid[X[i]]][cid[Y[j]]] = a[i][j]
    
    print("Yes")
    for i in range(H):
        print(*ans[i])


for _ in range(T):
    solve()
        
