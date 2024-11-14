from bisect import bisect_left, bisect_right
N = int(input())
X = list(map(int,input().split()))
P = list(map(int,input().split()))
Q = int(input())

S = [0]*(N+1)

for i in range(N):
  S[i+1] = S[i] + P[i]


for _ in range(Q):
  L, R = map(int,input().split())
  LX, RX= bisect_left(X, L), bisect_right(X, R)
  print(S[RX] - S[LX])
  
