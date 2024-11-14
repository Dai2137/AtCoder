S = input()
T = input()
if S==T:
    print(0)
    exit()

if len(S)<len(T):
    S += "*" * (len(T) - len(S))
elif len(T)<len(S):
    T += "*" * (len(S) - len(T))

for i in range(len(S)):
    if S[i] != T[i]:
        print(i+1)
        exit()