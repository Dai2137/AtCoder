from itertools import permutations
import math

N, S, T = map(int,input().split())
A, B, C, D = [], [], [], []

for _ in range(N):
    a, b, c, d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# 照射時間は不変
rasor = 0
for i in range(N):
   rasor += math.sqrt((A[i] - C[i]) ** 2 + (B[i] - D[i]) ** 2)

rasor /= T

not_rasor_min = 10 ** 10
# 線分の順番を固定
for path in permutations(range(N)):
    # それぞれの線分のどっちから先に照射するかを固定
    for i in range(2 ** N):
        time = 0
        nowx = 0
        nowy = 0
        for j in range(N):
            if ((i>>(N - 1 - j)) & 1):
                time += (math.sqrt((A[path[j]] - nowx) ** 2 + (B[path[j]] - nowy) ** 2)) / S
                nowx, nowy = C[path[j]], D[path[j]]
            else:
                time += (math.sqrt((C[path[j]] - nowx) ** 2 + (D[path[j]] - nowy) ** 2)) / S
                nowx, nowy = A[path[j]], B[path[j]]
        not_rasor_min = min(not_rasor_min, time)

print(rasor + not_rasor_min)
