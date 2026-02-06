from bisect import bisect_left
N, T = map(int, input().split())
A = list(map(int, input().split()))

now = 0
cnt  = 0

if N == 0:
    print(T)
    exit()


if A[-1] < T:
    A.append(T)
    N += 1


while now < T:
    next = bisect_left(A, now)
    if next == N:
        break
    now = A[next]
    
    if now + 100 <= T:
        now += 100
        cnt += 100
    else:
        cnt += T - now
        break

print(T - cnt)