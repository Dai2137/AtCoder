N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

ans = 1
for k in range(1,N+1):
  if ans >= k:
    ans = A[ans - 1][k - 1]
  else:
    ans = A[k - 1][ans - 1]

print(ans)