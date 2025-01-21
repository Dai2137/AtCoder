# from sortedcontainers import SortedList
# N = int(input())
# A = list(map(int,input().split()))
# S = SortedList(A)
# ans = 0

# while len(S)>=2:
#     s = S.bisect_left(2 * S[0])
#     if s == len(S):
#         break
#     ans += 1
#     S.pop(s)
#     S.pop(0)
# print(ans)
    
N = int(input())
A = list(map(int,input().split()))

ok = -1
ng = N//2 + 1

while ng - ok > 1:
    m = (ok + ng) // 2
    flg = True
    for i in range(m):
        if 2 * A[i] > A[N - m + i]:
            flg = False
            break
    if flg:
        ok = m
    else:
        ng = m
print(ok)