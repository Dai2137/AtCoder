N = int(input())

M = 1000000


def f(x):
    ans = 0
    while x > 0:
        ans += (x % 10) * (x % 10)
        x //= 10
    return ans
        

ans = False

for i in range(M):
    N = f(N)
    if N == 1:
        ans = True
        break

print("Yes" if ans else "No")