from bisect import bisect_left

N, A, B = map(int, input().split())
S = input()

# apos = []
# bpos = []

# for i, s in enumerate(S):
#     if s == "a":
#         apos.append(i)
#     elif s == "b":
#         bpos.append(i)

# ans = 0

# INF = N + 1

# for l in range(N):
#     ia = bisect_left(apos, l)
#     ia_need = ia + A - 1
#     if ia_need >= len(apos):
#         continue
#     rA = apos[ia_need]
    
#     ib = bisect_left(bpos, l)
#     ib_need = ib + B - 1
#     rB = bpos[ib_need] if ib_need < len(bpos) else INF
    
#     R_max = min(rB - 1, N - 1)
#     if rA <= R_max:
#         ans += R_max - rA + 1
    
# print(ans)

# 尺取り法
ra, rb, ca, cb, ans = 0, 0, 0, 0, 0
for l in range(N):
    while ra < N and ca < A:
        if S[ra] == 'a':
            ca += 1
        ra += 1
    if ra == N and ca < A:
        ra += 1
    while rb < N and cb < B:
        if S[rb] == 'b':
            cb += 1
        rb += 1
    if rb == N and cb < B:
        rb += 1
    
    ans += max(0, rb - ra)
    
    if S[l] == 'a':
        ca -= 1
    elif S[l] == 'b':
        cb -= 1
    
print(ans)
    
    
