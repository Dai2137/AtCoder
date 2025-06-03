N, M = map(int, input().split())
A = list(map(int, input().split()))

def judge(A_copy):
    n = len(A_copy)
    ans = True
    
    for i in range(1, M + 1):
        if i not in A_copy:
            ans = False
            break
    return ans

for i in range(N + 1):
    A_copy = A[:N - i].copy()
    flag = judge(A_copy)
    if not flag:
        print(i)
        exit()
