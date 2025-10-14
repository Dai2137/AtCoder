N, L, R = map(int, input().split())
S = input()

print("Yes" if S[L-1:R] == 'o'*(R-L+1) else "No")
