X, Y = map(int, input().split())

print((X + Y) % 12 if (X + Y) % 12 != 0 else 12)
