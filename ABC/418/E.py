import math
N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]

dx_dy_dict = {}
daikei_set = set()
for dot_i in range(N):
    for dot_j in range(dot_i + 1, N):
        dot_1 = dots[dot_i]
        dot_2 = dots[dot_j]
        if dot_2[0] - dot_1[0] < 0:
            dot_1, dot_2 = dot_2, dot_1
        dist = (dot_2[0] - dot_1[0]) ** 2 + (dot_2[1] - dot_1[1]) ** 2
        dx = dot_2[0] - dot_1[0]
        dy = dot_2[1] - dot_1[1]
        if dx == 0:
            dy = 1
        elif dy == 0:
            dx = 1
        else:
            gcd = math.gcd(dx, dy)
            dx //= gcd
            dy //= gcd

        if (dx, dy) in dx_dy_dict:
            dx_dy_dict[(dx, dy)].append((dot_i, dot_j, dist))
        else:
            dx_dy_dict[(dx, dy)] = [(dot_i, dot_j, dist)]

ans = 0
res = 0
for dx, dy in dx_dy_dict:
    n = len(dx_dy_dict[(dx, dy)])
    if n == 1:
        continue
    ans += n * (n - 1) // 2
    dist_dict = {}
    for i in range(n):
        if dx_dy_dict[(dx, dy)][i][2] in dist_dict:
            dist_dict[dx_dy_dict[(dx, dy)][i][2]] += 1
        else:
            dist_dict[dx_dy_dict[(dx, dy)][i][2]] = 1
    for dist in dist_dict:
        res += dist_dict[dist] * (dist_dict[dist] - 1) // 2
ans -= res // 2
# print(dx_dy_dict)
# print(dist_dict)
print(ans)
