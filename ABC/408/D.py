T = int(input())

def solve():
    N = int(input())
    S = list(input())
    
    r1 = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        r1[i] = r1[i + 1] + (S[i] == '1')
    
    ans = 10 ** 18
    lr0 = 0
    l10 = 0
    best = 0
    
    for r in range(1, N + 1):
        lr0 += (S[r - 1] == '0')
        l10 += (S[r - 1] == '1') - (S[r - 1] == '0')
        best = min(best, l10)
        ans = min(ans, lr0 + best + r1[r])
    
    print(ans)

for _ in range(T):
    solve()
