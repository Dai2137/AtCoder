# from bisect import bisect_left
N = int(input())


for d in range(1, 10 ** 6 + 1):
    if N % d == 0:
        ng = 10 ** 9 + 1
        ok = 1
        while ng - ok > 1:
            m = (ok + ng) // 2
            if 3 * m ** 2 + 3 * d * m + d ** 2 <= N // d:
                ok = m
            else:
                ng = m
        # print(ok)
        if 3 * ok ** 2 + 3 * d * ok + d ** 2 == N // d:
            print(ok + d, ok)
            exit()
        
            
print(-1)
    

