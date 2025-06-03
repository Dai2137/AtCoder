h, w, x, y = map(int, input().split())
s = []

for _ in range(h):
    s.append(input())

T = input()

x -= 1
y -= 1

gone = [[False] * w for _ in range(h)] 

cnt = 0
for Ti in T:
    if Ti == 'U' and x - 1 >= 0 and s[x - 1][y] != '#':
        x -= 1
        if s[x][y] == '@' and not gone[x][y]:
            cnt += 1
            gone[x][y] = True
    
    elif Ti == 'D' and x + 1 < h and s[x + 1][y] != '#':
        x += 1
        if s[x][y] == '@' and not gone[x][y]:
            cnt += 1
            gone[x][y] = True
    
    elif Ti == 'L' and y - 1 >= 0 and s[x][y - 1] != '#':
        y -= 1
        if s[x][y] == '@' and not gone[x][y]:
            cnt += 1
            gone[x][y] = True
    
    elif Ti == 'R' and y + 1 < w and s[x][y + 1] != '#':
        y += 1
        if s[x][y] == '@' and not gone[x][y]:
            cnt += 1
            gone[x][y] = True
            
print(x + 1, y + 1, cnt)   
# print(gone) 
    