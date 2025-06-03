import sys

input = sys.stdin.readline

N, K = map(int, input().split())
T = [[] for _ in range(N * K)]
for _ in range(N * K - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    T[u].append(v)
    T[v].append(u)
st = [(0, -1, 0)]
size = [1] * (N * K)
while st:
    v, p, t = st.pop()
    if t == 0:
        st.append((v, p, 1))
        for u in T[v]:
            if u != p:
                st.append((u, v, 0))
    else:
        cnt = 0
        for u in T[v]:
            if u != p:
                size[v] += size[u]
                if size[u] > 0:
                    cnt += 1
        if size[v] > K or cnt >= 3:
            print("No")
            exit()
        if size[v] < K and cnt >= 2:
            print("No")
            exit()
        if size[v] == K:
            size[v] = 0
print("Yes")
