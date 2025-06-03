N, M, Q = map(int, input().split())

allgivenusers = set()
user_given = [set() for _ in range(N)]

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        X, Y = q[1] - 1, q[2] - 1    
        user_given[X].add(Y)
    elif q[0] == 2:
        X = q[1] - 1
        allgivenusers.add(X)
    elif q[0] == 3:
        X, Y = q[1] - 1, q[2] - 1
        if X in allgivenusers:
            print("Yes")
        else:
            if Y in user_given[X]:
                print("Yes")
            else:
                print("No")
            
    
        