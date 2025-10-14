T = int(input())

def solve():
    N, M, K = map(int, input().split())
    S = input()
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)

    dp = [[False] * N for _ in range(2 * K + 1)]
    for i in range(N):
        if S[i] == 'A':
            dp[2 * K][i] = True
        else:
            dp[2 * K][i] = False
            
    for i in range(2 * K - 1, -1, -1):
        for j in range(N):
            if i % 2 == 0:
                alice_win = False
                for v in G[j]:
                    if dp[i + 1][v]:
                        alice_win = True
                        break
                dp[i][j] = alice_win
            else:
                bob_win = False
                for v in G[j]:
                    if not dp[i + 1][v]:
                        bob_win = True
                        break
                dp[i][j] = not bob_win
    print("Alice" if dp[0][0] else "Bob")


for _ in range(T):
    solve()
