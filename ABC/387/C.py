L, R = map(int, input().split())

def snake(S):
    ans = 0
    n = len(S)-1
    if n >= 2:
        for i in range(1, n):
            for j in range(1,10):
                ans += j ** i
            