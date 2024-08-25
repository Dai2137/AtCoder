N=int(input())
S=[input() for i in range(N)]

M=0
for i in range(N):
  M=max(M,len(S[i]))


T=[None] * M

for i in range(M):
  # T[i]
  T[i]=""
  for j in reversed(range(N)):
    if i < len(S[j]):
      T[i] += S[j][i]
    else:
      T[i] += "*"

for j in range(M):
  trimmed_string = T[j].rstrip('*')
  print(trimmed_string) 

# for i in reversed(range(N)):
#   print(i)

# for j in range(M):
#   # trimmed_string = T[j].rstrip('*')
#   print(T[j]) 

