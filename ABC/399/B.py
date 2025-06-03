N = int(input())

P = list(map(int, input().split()))

rank = [None] * N

r = 1

while None in rank:
    # print(0)
    m = max(P)
    k = 0
    for i in range(N):
        if rank[i] == None and P[i] == m:
            k += 1
            rank[i] = r
            P[i] = 0
    
    r += k

for i in range(N):
    print(rank[i])
