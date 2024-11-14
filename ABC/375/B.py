import math

def calc_dist(a,b,c,d):
    return math.sqrt((a - c)**2 + (b - d)**2)

N = int(input())
now = [0, 0]
ans = 0.0

for i in range(N):
    X, Y = map(int,input().split())
    ans += calc_dist(now[0], now[1], X, Y)
    now = [X, Y]
    if i==N-1:
        ans += calc_dist(now[0], now[1], 0, 0)

print(ans)
