import math
N = int(input())

# se = set()
for i in range(100):
    if 2 ** i > N:
        t = i
        break

t -= 1
ans = 0
for i in range(1, t + 1):
    upper = N // (1 << i)
    b_max = int(math.isqrt(upper))
    # 二分探索でもいいな
    ans += (b_max + 1) // 2
print(ans)
        
    