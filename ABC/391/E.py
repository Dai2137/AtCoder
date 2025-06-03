from more_itertools import chunked
N = int(input())
A = list(input())
B = [A.copy()]
A_temp = A.copy()
for i in range(N):
    chunk = chunked(A_temp, 3)
    temp = []
    for lst in chunk:
        if lst.count('1') >= 2:
            temp.append('1')
        else:
            temp.append('0')
    
    B.append(temp)
    A_temp = temp
            

def f_1(i: int , j: int):
    if i == 0:
        return 1
    if B[i-1][3*j: 3*j + 3].count('1') == 3:
        return f_1(i-1, 3*j) + f_1(i-1, 3*j + 1) + f_1(i-1, 3*j + 1) - max(f_1(i-1, 3*j), f_1(i-1, 3*j + 1), f_1(i-1, 3*j + 1))
    else:
        temp = 10 ** 10
        for k in range(3):
            if B[i-1][3 * j + k] == '1':
                temp = min(f_1(i - 1, 3 * j + k), temp)
        return temp

def f_0(i: int , j: int):
    if i == 0:
        return 1
    if B[i-1][3*j: 3*j + 3].count('0') == 3:
        return f_1(i-1, 3*j) + f_1(i-1, 3*j + 1) + f_1(i-1, 3*j + 1) - max(f_1(i-1, 3*j), f_1(i-1, 3*j + 1), f_1(i-1, 3*j + 1))
    else:
        temp = 10 ** 10
        for k in range(3):
            if B[i-1][3 * j + k] == '0':
                temp = min(f_1(i - 1, 3 * j + k), temp)
        return temp

if B[-1] == ['1']:
    print(f_1(N, 0))
else:
    print(f_0(N, 0))
    
