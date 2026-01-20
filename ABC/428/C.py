Q = int(input())
S = [0]
INF = 10**18

# for _ in range(Q):
#     q = input().split()
#     if q[0] == "1":
#         c = q[1]
#         if c == "(":
#             S.append(S[-1] + 1)
#         else:
#             if S[-1] != 0:
#                 S.append(S[-1] - 1)
#             else:
#                 S.append(S[-1] - INF)
#     else:
#         S.pop()
#     if S[-1] == 0:
#         print("Yes")
#     else:
#         print("No")
# min_S = [0]
# for _ in range(Q):
#     q = input().split()
#     if q[0] == "1":
#         c = q[1]
#         if c == "(":
#             min_S.append(min(min_S[-1], S[-1] + 1))
#             S.append(S[-1] + 1)
#         else:
#             min_S.append(min(min_S[-1], S[-1] - 1))
#             S.append(S[-1] - 1)
#     else:
#         min_S.pop()
#         S.pop()
#     if min_S[-1] >= 0 and S[-1] == 0:
#         print("Yes")
#     else:
#         print("No")

num_lower_than_0 = [0]
for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        c = q[1]
        if c == "(":
            num_lower_than_0.append(num_lower_than_0[-1])
            S.append(S[-1] + 1)
        else:
            if S[-1] == 0:
                num_lower_than_0.append(num_lower_than_0[-1] + 1)
            else:
                num_lower_than_0.append(num_lower_than_0[-1])
            S.append(S[-1] - 1)
    else:
        num_lower_than_0.pop()
        S.pop()
    if num_lower_than_0[-1] == 0 and S[-1] == 0:
        print("Yes")
    else:
        print("No")

