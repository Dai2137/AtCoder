# from bisect import bisect_left, bisect_right
N, M = map(int, input().split())

B = list(map(int, input().split()))
W = list(map(int, input().split()))

B.sort(reverse=True)
W.sort(reverse=True)

b = 0
while b < N and B[b] >= 0:
    b += 1
    
w = 0
while w < M and W[w] > 0:
    w += 1

if B[0] < 0:
    ans = 0
    for i in range(min(N, M)):
        if B[i] + W[i] < 0:
            break
        else:
            ans += B[i] + W[i]
        # break
    print(ans)
    exit()
else:
    # b = bisect_right(B, 0)
    # w = bisect_left(W, 0)
    ans = sum(B[:b])
    # print(b, w)
    # print(ans)
    if w <= b:
        ans += sum(W[:w])
        print(ans)
        exit()
    else:
        ans += sum(W[:b])
        for i in range(b, min(N, M)):
            if B[i] + W[i] < 0:
                break
            else:
                ans += B[i] + W[i]
        print(ans)
        

