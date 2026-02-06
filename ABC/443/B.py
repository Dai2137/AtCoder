N, K = map(int, input().split())

ans = 0
cnt = 0
while cnt < K:
    ans += 1
    cnt += N
    N += 1

print(ans - 1)