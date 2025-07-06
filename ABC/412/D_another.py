from itertools import combinations, permutations

N, M = map(int, input().split())

G = [[0] * N  for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a][b] = G[b][a] = 1
ans = 10 ** 18

def dist(G_1, G_2):
    d = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if G_1[i][j] != G_2[i][j]:
                d += 1
    return d

for e in permutations(range(N)):
    G_2 = [[0] * N  for _ in range(N)]
    for i in range(N):
        if i + 1 < N:
            G_2[e[i]][e[i + 1]] = G_2[e[i + 1]][e[i]] = 1
        else:
            G_2[e[i]][e[0]] = G_2[e[0]][e[i]] = 1
    ans = min(ans, dist(G, G_2))

if N == 6:
    for e in combinations(range(N), 3):
        G_2 = [[0] * N  for _ in range(N)]
        for i in range(3):
            if i + 1 < 3:
                G_2[e[i]][e[i + 1]] = G_2[e[i + 1]][e[i]] = 1
            else:
                G_2[e[i]][e[0]] = G_2[e[0]][e[i]] = 1
        another = [i for i in range(N) if i not in e]
        for i in range(3):
            if i + 1 < 3:
                G_2[another[i]][another[i + 1]] = G_2[another[i + 1]][another[i]] = 1
            else:
                G_2[another[i]][another[0]] = G_2[another[0]][another[i]] = 1
        ans = min(ans, dist(G, G_2))

elif N == 7:
    for e_1 in combinations(range(N), 4):
        for e_2 in permutations(e_1):
            G_2 = [[0] * N  for _ in range(N)]
            for i in range(4):
                if i + 1 < 4:
                    G_2[e_2[i]][e_2[i + 1]] = G_2[e_2[i + 1]][e_2[i]] = 1
                else:
                    G_2[e_2[i]][e_2[0]] = G_2[e_2[0]][e_2[i]] = 1
            another = [i for i in range(N) if i not in e_1]
            for i in range(3):
                if i + 1 < 3:
                    G_2[another[i]][another[i + 1]] = G_2[another[i + 1]][another[i]] = 1
                else:
                    G_2[another[i]][another[0]] = G_2[another[0]][another[i]] = 1
            ans = min(ans, dist(G, G_2))

elif N == 8:
    for e_1 in combinations(range(N), 5):
        for e_2 in permutations(e_1):
            G_2 = [[0] * N  for _ in range(N)]
            for i in range(5):
                if i + 1 < 5:
                    G_2[e_2[i]][e_2[i + 1]] = G_2[e_2[i + 1]][e_2[i]] = 1
                else:
                    G_2[e_2[i]][e_2[0]] = G_2[e_2[0]][e_2[i]] = 1
            another = [i for i in range(N) if i not in e_1]
            for i in range(3):
                if i + 1 < 3:
                    G_2[another[i]][another[i + 1]] = G_2[another[i + 1]][another[i]] = 1
                else:
                    G_2[another[i]][another[0]] = G_2[another[0]][another[i]] = 1
            ans = min(ans, dist(G, G_2))
    
    for e_1 in combinations(range(N), 4):
        for e_2 in permutations(e_1):
            another = [i for i in range(N) if i not in e_1]
            for e_3 in permutations(another):
                G_2 = [[0] * N  for _ in range(N)]
                for i in range(4):
                    if i + 1 < 4:   
                        G_2[e_2[i]][e_2[i + 1]] = G_2[e_2[i + 1]][e_2[i]] = 1
                    else:
                        G_2[e_2[i]][e_2[0]] = G_2[e_2[0]][e_2[i]] = 1
            
                for i in range(4):
                    if i + 1 < 4:
                        G_2[e_3[i]][e_3[i + 1]] = G_2[e_3[i + 1]][e_3[i]] = 1
                    else:
                        G_2[e_3[i]][e_3[0]] = G_2[e_3[0]][e_3[i]] = 1
                ans = min(ans, dist(G, G_2))
        
print(ans)
        
