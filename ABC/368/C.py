N=int(input())
H=list(map(int,input().split()))

T=0

t=0

for i in range(N):
  T += (-t) + ((H[i] + t) // 5) * 3 + min((H[i] + t) % 5, 3)
  if 1<=(H[i] + t) % 5<=2:
    t = (H[i] + t) % 5
  else:
    t=0

print(T)