from atcoder.fenwicktree import FenwickTree

N = int(input())
S = input()

# ft = FenwickTree(2 * N + 1)

# AB = [0] * N
# for i in range(N):
#     if S[i] == 'A':
#         AB[i] = 1
#     if S[i] == 'B':
#         AB[i] = -1

# D = [0] * (N + 1)
# for i in range(N):
#     D[i + 1] = D[i] + AB[i]

# for i in range(N + 1):
#     D[i] += N

# ans = 0
# for i in range(N + 1):
#     ft.add(D[i], 1)
#     ans += ft.sum(0, D[i])

cnt = [0] * (2 * N + 1)
cnt[N] = 1
x = N
sum = 0
ans = 0
for i in range(N):
    if S[i] == 'A':
        sum += cnt[x]
        x += 1
        cnt[x] += 1
    elif S[i] == 'B':
        sum -= cnt[x - 1]
        x -= 1
        cnt[x] += 1
    else:
        cnt[x] += 1

    ans += sum
    
print(ans)