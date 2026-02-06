


T = int(input())


for _ in range(T):
    N, C = map(int, input().split())
    C -= 1
    S = [input() for _ in range(N)]
    reachable_limit = [N] * N
    for j in range(N):
        wall_broken = False
        for i in range(N - 1, -1, -1):
            if S[i][j] == '.':
                reachable_limit[j] = i
            elif S[i][j] == '#' and not wall_broken:
                reachable_limit[j] = i
                wall_broken = True
                break
            else:
                break
    dp = [False] * N
    dp[C] = True
    
    for i in range(N - 1, 0, -1):
        next_dp = [False] * N
        for j in range(N):
            if dp[j]:
                for nj in range(max(0, j - 1), min(N, j + 2)):
                    if reachable_limit[nj] <= i - 1:
                        next_dp[nj] = True
        dp = next_dp
        if not any(dp):
            break
    
    res = "".join(['1' if x else '0' for x in dp])
    print(res)
