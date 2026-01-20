P, Q = map(int, input().split())
X, Y = map(int, input().split())

print("Yes" if P <= X <= P + 99 and Q <= Y <= Q + 99 else "No")