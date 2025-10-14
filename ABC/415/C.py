# T = int(input())
# from atcoder.dsu import DSU

# def solve():
#     N = int(input())
#     S = input()
#     uf = DSU(2 ** N)
#     for i in range(2 ** N - 1):
#         if i - 1 >= 0 and S[i - 1] == '1':
#             continue
#         for j in range(N):
#             if (i >> j) & 1:
#                 continue
#             if S[i + (1 << j) - 1] == '0':
#                 uf.merge(i, i + (1 << j))

#     print("Yes" if uf.same(0, 2 ** N - 1) else "No")


# for _ in range(T):
#     solve()


from collections import deque

def can_mix_all(N, S):
    safe = [s == '0' for s in S]
    visited = [False] * (1 << N)
    visited[0] = True
    q = deque([0])

    while q:
        cur = q.popleft()
        for i in range(N):
            if not (cur >> i) & 1:  # 薬品iが未投入
                nxt = cur | (1 << i)
                if safe[nxt - 1] and not visited[nxt]:  # 状態が安全
                    visited[nxt] = True
                    q.append(nxt)
    return visited[(1 << N) - 1]

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    print("Yes" if can_mix_all(N, S) else "No")
