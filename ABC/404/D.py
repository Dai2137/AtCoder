def get_kth_trit(i, k):
    return (i // (3 ** k)) % 3

N, M = map(int, input().split())
C = list(map(int, input().split()))

K = []
A = []
for i in range(M):
    k, *a = map(int, input().split())
    # *aの要素を全て-1
    a = [x - 1 for x in a]
    K.append(k)
    A.append(a)

ans = 10 ** 20

for i in range(3 ** N):
    for j in range(M):
        cnt = 0
        for Ajk in A[j]:
            cnt += get_kth_trit(i, Ajk)
        if cnt < 2:
            break
    if cnt < 2:
        continue
    
    ans = min(ans, sum([C[k] * get_kth_trit(i, k) for k in range(N)]))

print(ans)
    
    