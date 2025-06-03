from bisect import bisect_left
N, S =map(int, input().split())
A  = list(map(int, input().split()))

tot = sum(A)

S = S % tot

dA = 2 * A

adS = [0] * (2 * N + 1)


# for i in range(2 * N):
#     adS[i + 1] = adS[i] + dA[i]

# for i in range(1, 2 * N + 1):
#     if adS[i] < S: continue
#     if adS[i] == S:
#         print("Yes")
#         exit()
#     Sa = adS[i] - S
#     j = bisect_left(adS, Sa)
#     if adS[j] == Sa:
#         print("Yes")
#         exit()

# print("No")

se = set()
for i in range(2 * N):
    adS[i + 1] = adS[i] + dA[i]
    se.add(adS[i + 1])

for i in range(1, 2 * N + 1):
    if adS[i] < S: continue
    if adS[i] == S:
        print("Yes")
        exit()
    Sa = adS[i] - S
    if Sa in se:
        print("Yes")
        exit()
    # j = bisect_left(adS, Sa)
    # if adS[j] == Sa:
    #     print("Yes")
    #     exit()

print("No")
    
