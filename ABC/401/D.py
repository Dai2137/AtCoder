N, K = map(int, input().split())
S = input()

T = [None] * N

for i in range(N):
    if S[i] == 'o':
        T[i] = 'o'
    elif S[i] == '.':
        T[i] = '.'
# print(T)
cnt = 0
for i in range(N):
    if S[i] == 'o':
        cnt += 1
        if i - 1 >= 0:
            T[i - 1] = '.'
        if i + 1 < N:
            T[i + 1] = '.'

lr = []
i = 0
while i < N:
    if T[i] == None:
        l = i
        while i < N and T[i] == None:
            i += 1
        r = i
        lr.append((l, r))
    else:
        i += 1

max_cnt = 0
for l, r in lr:
    max_cnt += (r - l + 1) // 2

rest = K - cnt

if rest == 0:
    for i in range(N):
        if T[i] == None:
            T[i] = '.'
elif rest != max_cnt:
    for i in range(N):
        if T[i] == None:
            T[i] = '?'
else:
    for l, r in lr:
        if (r - l) % 2 == 0:
            for i in range(l, r):
                T[i] = '?'
        else:
            maru = True
            for i in range(l, r):
                if maru:
                    T[i] = 'o'
                else:
                    T[i] = '.'
                maru = not maru                

print(''.join(T))