A, B, C, D = map(int, input().split())

if A < C:
    print("No")
elif A > C:
    print("Yes")
else:
    if B < D:
        print("No")
    else:
        print("Yes")