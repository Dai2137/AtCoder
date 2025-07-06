S = input()
T = input()

ans = True
for i in range(1, len(S)):
    # もし大文字なら
    if S[i].isupper():
        if S[i - 1] not in T:
            ans = False

print("Yes" if ans else "No")
    
