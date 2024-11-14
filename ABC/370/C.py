S = list(input())
T = list(input())

# Done = [False] * len(S)

M = 0
X = []
for i in range(len(S)):
  if ord(S[i]) > ord(T[i]):
    S[i] = T[i]
    X.append(''.join(S))
    M += 1

for i in reversed(range(len(S))):
  if ord(S[i]) < ord(T[i]):
    S[i] = T[i]
    X.append(''.join(S))
    M += 1

print(M)
for m in range(M):
  print(X[m])