N = int(input())
H = list(map(int, input().split()))

ans = 0
for w in range(1, N + 1):
    for si in range(w):
        a = []
        i = si
        while i < N:
            a.append(H[i])
            i += w
        
        val = -1
        le = 0
        for ai in a:
            if ai == val:        
                le += 1
            else:
                le = 1
                val = ai
            ans = max(ans, le)

print(ans)