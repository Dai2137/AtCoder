N,M = map(int,input().split())
isoccupied = set()
ans = N**2

def voidcheck(a, b):
    if 0<=a<N and 0<=b<N and (a,b) not in isoccupied:
        return True
    else:
        return False

dxdy = [(0,0), (2,1), (1,2), (-1, 2), (-2,1), (-2,-1), (-1,-2), (1, -2), (2,-1)]

for m in range(M):
    a,b = map(int,input().split())
    a,b = a-1, b-1

    for dx, dy in dxdy:
        if voidcheck(a+dx,b+dy):
            ans -= 1
            isoccupied.add((a+dx,b+dy))
            # print((a+dx, b+dy))

print(ans)
