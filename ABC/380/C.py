from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] 
def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

N, K = map(int, input().split())
S = input()
S_run = runLengthEncode(S)
num_1 = 0
S_idx = 0
for i in range(len(S_run)):
    if S_run[i][0] == '1':
        num_1 += 1
        if num_1 == K:
            idx_1 = S_idx
            cnt_1 = S_run[i][1]
            idx_0 = idx_1 - S_run[i-1][1]
            cnt_0 = S_run[i-1][1]
            break
    S_idx += S_run[i][1]

list_S = list(S)
for i in range(idx_0, idx_0 + cnt_1):
    list_S[i] = '1'
for i in range(idx_1, idx_1 + cnt_0):
    list_S[i] = '0'
print(''.join(list_S))