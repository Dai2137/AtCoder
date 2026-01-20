N, Q = map(int, input().split())
A = list(map(int, input().split()))

M = 30

to = [[0] * N for _ in range(M)]
cost = [[0] * N for _ in range(M)]

for i in range(N):
    to[0][i] = A[i] - 1
    cost[0][i] = i + 1

for i in range(1, M):
    for j in range(N):
        to[i][j] = to[i - 1][to[i - 1][j]]
        cost[i][j] = cost[i - 1][j] + cost[i - 1][to[i - 1][j]]

for _ in range(Q):
    T, B = map(int, input().split())
    B -= 1
    ans = 0
    for k in range(M):
        if (T >> k) & 1:
            ans += cost[k][B]
            B = to[k][B]
    print(ans)






# import sys
# from array import array

# N, Q = map(int, input().split())
# A = [0] + list(map(int, input().split()))  

# LOG = 31  

# up = []
# sm = []

# up0 = array('I', [0]) * (N + 1)
# sm0 = array('Q', [0]) * (N + 1)
# for v in range(1, N + 1):
#     up0[v] = A[v]
#     sm0[v] = v  
# up.append(up0)
# sm.append(sm0)

# for k in range(1, LOG):
#     prev_up = up[k - 1]
#     prev_sm = sm[k - 1]
#     cur_up = array('I', [0]) * (N + 1)
#     cur_sm = array('Q', [0]) * (N + 1)
#     for v in range(1, N + 1):
#         mid = prev_up[v]
#         cur_up[v] = prev_up[mid]
#         cur_sm[v] = prev_sm[v] + prev_sm[mid]
#     up.append(cur_up)
#     sm.append(cur_sm)

# out = []
# for _ in range(Q):
#     T, B = map(int, input().split())
#     cur = B
#     res = 0
#     k = 0
#     while T:
#         if T & 1:
#             res += sm[k][cur]
#             cur = up[k][cur]
#         T >>= 1
#         k += 1
#     out.append(str(res))

# print("\n".join(out))