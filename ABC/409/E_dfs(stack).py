N = int(input())
x = list(map(int, input().split()))
T = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    T[u].append((v, w))
    T[v].append((u, w))

ans = 0
st = [(0, -1, 0)]
while st:
    v, p, t = st.pop()
    if t == 0:
        st.append((v, p, 1))
        for u, w in T[v]:
            if u != p:
                st.append((u, v, 0))
    else:
        for u, w in T[v]:
            if u == p:
                continue
            ans += w * abs(x[u])
            x[v] += x[u]
print(ans)
