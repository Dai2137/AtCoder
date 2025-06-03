N = int(input())
out = True
ans = 0
for i in range(N):
    S = input()
    if S == "login":
        out = False
        
    elif S == "logout":
        out = True
    elif S == "private" and out:
        ans += 1

print(ans)