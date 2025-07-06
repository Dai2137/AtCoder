# T = int(input())

# def solve():
#     N = int(input())
#     S = list(map(int, input().split()))
#     S_sub = S[1: N - 1]
#     S_sub.sort()
#     for i in range(N - 2):
#         if S_sub[i] >= S[N - 1]:
#             break
#     S_sub = S_sub[:i]
#     S = [S[0]] + S_sub + [S[N - 1]]
#     i = 0
#     cnt = 0
#     N = len(S)
#     while i < N - 1:
#         if 2 * S[i] >= S[-1]:
#             cnt += 1
#             break
#         else:
#             j = i + 1
#             if 2 * S[i] < S[j]:
#                 print(-1)
#                 return
#             while 2 * S[i] >= S[j]:
#                 j += 1
#             i = j - 1
#             cnt += 1
#     print(cnt)
            
    

# for _ in range(T):
#     solve()

T = int(input())

def solve():
    N = int(input())
    S = list(map(int, input().split()))
    S_sub = S[1: N - 1]
    S_sub.sort()

    # S[N - 1] より小さい要素だけを残す
    trimmed_sub = []
    for x in S_sub:
        if x >= S[N - 1]:
            break
        trimmed_sub.append(x)

    S = [S[0]] + trimmed_sub + [S[N - 1]]
    i = 0
    cnt = 1
    N = len(S)

    while i < N - 1:
        if 2 * S[i] >= S[-1]:
            cnt += 1
            break
        else:
            j = i + 1
            while j < N and 2 * S[i] >= S[j]:
                j += 1
            if j == i + 1:
                print(-1)
                return
            i = j - 1
            cnt += 1
    print(cnt)

for _ in range(T):
    solve()
