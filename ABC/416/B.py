S = input()
N = len(S)
T = [None] * N
sharp_idxs = []
for i in range(N):
    if S[i] == '#':
        T[i] = '#'
        sharp_idxs.append(i)

if not sharp_idxs:
    T = ['o'] + ['.'] * (N - 1)
    print(''.join(T))
    exit()

if sharp_idxs[0] != 0:
    T[0] = 'o'

for i in sharp_idxs:
    if i + 1 < N and T[i + 1] != '#':
        T[i + 1] = 'o'
for i in range(N):
    if T[i] == None:
        T[i] = '.'
print(''.join(T))
