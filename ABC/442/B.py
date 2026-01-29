Q = int(input())

if_play = False
count = 0

for _ in range(Q):
    A = int(input())
    if A == 1:
        count += 1
        
    if A == 2:
        if count > 0:
            count -= 1
    if A == 3:
        if_play = not if_play
    
    print("Yes" if if_play and count >= 3 else "No")
