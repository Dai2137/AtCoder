N = int(input())

ans = [[None] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    j = N + 1 - i
    if i <= j:
        if i % 2 == 1:
            for k in range(i, j + 1):
                for l in range(i, j + 1):
                    ans[k][l] = '#'
        else:
            for k in range(i, j + 1):
                for l in range(i, j + 1):
                    ans[k][l] = '.'
ansa =[]
for i in range(1, N + 1):
    ansa.append(''.join(ans[i][1:]))

for i in range(N):
    print(ansa[i])