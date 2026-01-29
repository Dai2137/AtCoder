import math
N, Q = map(int, input().split())

X, Y = [], []

for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(-y)

Y_pos = []
Y_neg = []


for i in range(N):
    norm = float(math.sqrt(X[i] ** 2 + Y[i] ** 2))
    X[i] /= norm
    Y[i] /= norm
    if Y[i] > 0 or (Y[i] == 0 and X[i] > 0):
        Y_pos.append((X[i], i))
    else:
        Y_neg.append((X[i], i))

Y_pos.sort(key=lambda x: x[0], reverse=True)
Y_neg.sort(key=lambda x: x[0])

from itertools import groupby

def runLengthEncode(S: list) -> "list[tuple(float, list)]":
    grouped = groupby(S, key=lambda x: x[0])
    res = []
    for k, v in grouped:
        res.append(list(map(lambda x: x[1], v)))
    return res

Y_pos_rle = runLengthEncode(Y_pos)
Y_neg_rle = runLengthEncode(Y_neg)

C = Y_pos_rle + Y_neg_rle

idx_to_Cidx = {}

for i in range(len(C)):
    for j in range(len(C[i])):
        idx_to_Cidx[C[i][j]] = i

C_num = []
for i in range(len(C)):
    C_num.append(len(C[i]))

C_num2 = C_num + C_num
C_cumsum = [0]
for i in range(len(C_num2)):
    C_cumsum.append(C_cumsum[-1] + C_num2[i])



for _ in range(Q):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    A_idx = idx_to_Cidx[A]
    B_idx = idx_to_Cidx[B]
    if A_idx > B_idx:
        B_idx += len(C)
    ans = C_cumsum[B_idx + 1] - C_cumsum[A_idx]
    print(ans)
    