S = list(input())
n = len(S)

S = S[:(n-1)//2] + S[(n+1)//2:]

print("".join(S))











