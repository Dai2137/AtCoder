from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))


A.sort()

# D = {}

# for i in range(N):
#     if A[i] not in D:
#         D[A[i]] = 0
#     for key in D:
#         D[key] += 1


def judge(x):
    ans = 0
    for i in range(N):
        if A[i] >= x:
            ans += 1
    if ans >= x:
        return True
    else:
        return False
            
ok = 0
ng = 10 ** 9 + 2

while ng - ok > 1:
    mid = (ok + ng) // 2
    if judge(mid):
        ok = mid
    else:
        ng = mid

print(ok)
  
          
# ans = -1
# for key in D:
#     if D[key] >= key:
#         ans = max(ans, key)

# print(ans)

