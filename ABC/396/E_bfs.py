from collections import deque

n, m = map(int,input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int,input().split())
    x-=1
    y-=1
    g[x].append((y, z))
    g[y].append((x, z))
    
visited = [False] * n

