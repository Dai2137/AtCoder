X, Y, Z = map(int, input().split())

if X < Y:
    print("No")
else:
    if abs(X - Y) % (Z - 1)  == 0:
        if abs(X - Y) // (Z - 1) >= min(X, Y):
            print("Yes")
        else:
            print("No")
    else:
        print("No")