T = int(input())

def solve():
    N = int(input())
    S = list(input())
    l = -1
    for i in range(N - 1):
        if S[i] > S[i + 1]:
            l = i
            break
    if l == -1:
        print(''.join(S))
        return
    else:
        for i in range(l + 1, N):
            if S[i] > S[l]:
                S = S[:l] + S[l + 1: i] + [S[l]] + S[i:]
                print(''.join(S))
                return
        S = S[:l] + S[l + 1:] + [S[l]]
        print(''.join(S))

for _ in range(T):
    solve()
