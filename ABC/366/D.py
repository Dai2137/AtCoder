N=int(input())
A=[[0]*N for i in range(N)]

for x in range(N):
  for y in range(N):
    A[x][y] = list(map(int,input().split()))

S=[[[0]*N for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            S[i][j][k] = A[i][j][k]
            if i > 0:
                S[i][j][k] += S[i-1][j][k]
            if j > 0:
                S[i][j][k] += S[i][j-1][k]
            if k > 0:
                S[i][j][k] += S[i][j][k-1]
            if i > 0 and j > 0:
                S[i][j][k] -= S[i-1][j-1][k]
            if i > 0 and k > 0:
                S[i][j][k] -= S[i-1][j][k-1]
            if j > 0 and k > 0:
                S[i][j][k] -= S[i][j-1][k-1]
            if i > 0 and j > 0 and k > 0:
                S[i][j][k] += S[i-1][j-1][k-1]

def sum_region(S, x1, y1, z1, x2, y2, z2):
    total = S[x2][y2][z2]
    if x1 > 0:
        total -= S[x1-1][y2][z2]
    if y1 > 0:
        total -= S[x2][y1-1][z2]
    if z1 > 0:
        total -= S[x2][y2][z1-1]
    if x1 > 0 and y1 > 0:
        total += S[x1-1][y1-1][z2]
    if x1 > 0 and z1 > 0:
        total += S[x1-1][y2][z1-1]
    if y1 > 0 and z1 > 0:
        total += S[x2][y1-1][z1-1]
    if x1 > 0 and y1 > 0 and z1 > 0:
        total -= S[x1-1][y1-1][z1-1]
    return total

Q=int(input())

for q in range(Q):
  Lx,Rx,Ly,Ry,Lz,Rz = map(int,input().split())
  print(sum_region(S,Lx-1,Ly-1,Lz-1,Rx-1,Ry-1,Rz-1))
