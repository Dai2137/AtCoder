N, R, C = map(int, input().split())

S = input()
smoke = set([(0, 0)])
fire = [0, 0]

ans = ""
for i in range(N):
    if S[i] == 'N':
        R += 1
        fire[0] += 1
    elif S[i] == 'W':
        C += 1
        fire[1] += 1
    if S[i] == 'S':
        R -= 1
        fire[0] -= 1
    if S[i] == 'E':
        C -= 1
        fire[1] -= 1
    
    if (R, C) in smoke:
        ans += '1'
    else:
        ans += '0'
    
    smoke.add((fire[0], fire[1]))

print(ans)