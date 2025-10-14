N, M = map(int, input().split())

AB = []

for _ in range(M):
    a, b = map(int, input().split())
    AB.append((a, b, a - b))

AB.sort(key=lambda x: x[2], reverse=True)
ans = 0
while AB:
    while AB and AB[-1][0] > N:
        AB.pop()
    if not AB:
        break
    a, b, c = AB.pop()
    num = (N - a) // c + 1
    ans += num
    N -= num * c

print(ans)
