N = int(input())
A = list(map(int, input().split()))

ans = 0
for si in range(2):
    cnt = [0] * (N + 1)
    r = si
    for l in range(si, N - 1, 2):
        while r + 1 < N:
            if A[r] != A[r + 1]:
                break
            if cnt[A[r]] > 0:
                break
            cnt[A[r]] += 1
            r += 2
        ans = max(ans, r - l)
        
        if l == r:
            r += 2
        else:
            cnt[A[l]] -= 1
        # print(l, r, cnt)

print(ans)
