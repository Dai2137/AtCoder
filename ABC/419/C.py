N = int(input())
R = []
C = []

for _ in range(N):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)

min_r = min(R)
max_r = max(R)
min_c = min(C)
max_c = max(C)

ans = max((max_r - min_r + 1) // 2, (max_c - min_c + 1) // 2)

print(ans)




