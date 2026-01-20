from collections import defaultdict
N = int(input())

n_cand = defaultdict(int)
for y in range(2, 3500):
    for x in range(1, y):
        if x ** 2 + y ** 2 > N:
            continue
        n_cand[x ** 2 + y ** 2] += 1

ans = []
for key, value in n_cand.items():
    if value == 1:
        ans.append(key)
ans.sort()
print(len(ans))
print(*ans)