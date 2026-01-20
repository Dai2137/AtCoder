N, M = map(int, input().split())
S = input()
T = input()
Q = int(input())

for _ in range(Q):
    W = input()
    t, a = True, True
    for w in W:
        if w not in S:
            t = False
        if w not in T:
            a = False
    if t and a:
        print("Unknown")
    elif t:
        print("Takahashi")
    else:
        print("Aoki")

