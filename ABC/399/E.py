N = int(input())
S = input()
T = input()

if S==T:
    print("0")
    exit()

C = 26
to = [-1] * 26
for i in range(N):
    sc, tc = ord(S[i]) - ord('a'), ord(T[i]) - ord('a')
    if to[sc] != -1 and to[sc] != tc:
       print('-1')
       exit()
    to[sc] = tc

