S, A, B, X = map(int, input().split())

t = 0

s = X // (A + B)
c = X % (A + B)

ans = s * S * A

if c <= A:
    ans += S * c
else:
    ans += S * A

print(ans)
