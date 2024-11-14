from itertools import permutations
N=int(input())
adj1 = [[0] * N for _ in range(N)]
adj2 = [[0] * N for _ in range(N)]

M1 = int(input())
for _ in range(M1):
  u,v = map(int,input().split())
  adj1[u-1][v-1] = adj1[v-1][u-1] = 1
M2 = int(input())
for _ in range(M2):
  u,v = map(int,input().split())
  adj2[u-1][v-1] = adj2[v-1][u-1] = 1

A = []
for i in range(N-1):
  row = list(map(int,input().split()))
  A.append([0]*(i+1) + row)

ans = 10**9

for p in permutations(range(N)):
  cost = 0
  for i in range(N-1):
    for j in range(i+1, N):
      if adj2[i][j] ^ adj1[p[i]][p[j]]:
        cost += A[i][j]
  ans = min(ans, cost)

print(ans)


# from itertools import permutations

# N = int(input())
# adj1 = [[0] * N for _ in range(N)]
# adj2 = [[0] * N for _ in range(N)]
# M1 = int(input())
# for _ in range(M1):
#     u, v = map(int, input().split())
#     adj1[u - 1][v - 1] = adj1[v - 1][u - 1] = 1
# M2 = int(input())
# for _ in range(M2):
#     a, b = map(int, input().split())
#     adj2[a - 1][b - 1] = adj2[b - 1][a - 1] = 1
# A = []
# for i in range(N - 1):
#     row = list(map(int, input().split()))
#     A.append([0] * (i + 1) + row)

# ans = 10**9
# for p in permutations(range(N)):
#     cost = 0
#     for i in range(N):
#         for j in range(i + 1, N):
#             if adj1[p[i]][p[j]] ^ adj2[i][j]:
#                 cost += A[i][j]
#     ans = min(ans, cost)
# print(ans)
