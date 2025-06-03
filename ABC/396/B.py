Q = int(input())

A = [0] * 100

for _ in range(Q):
    t, *x = map(int, input().split())    
    match t:
        case 1:
            # t=1 のときの処理
            x = x[0]
            # print(type(x))
            # print(x)
            A.append(x)

        case 2:
            # t=2 のときの処理
            
            print(A.pop())