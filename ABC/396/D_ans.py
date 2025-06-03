N, M = map(int, input().split())
G = [[] * N for i in range(N)]  # 隣接頂点リスト．（頂点, 辺のラベル）をペアで持つ．
for i in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))

ans = 1 << 60
visited = [False] * N  # 訪問済みかどうかを持つリスト


def dfs(v, xor):
    global ans
    visited[v] = True  # 頂点 v を訪問済みにする

    # もし今いる頂点が N - 1 なら答えを更新する
    if v == N - 1:
        ans = min(ans, xor)

    for u, w in G[v]:
        # もし頂点 u に訪れていないなら，頂点 u に進む
        if not visited[u]:
            dfs(u, xor ^ w)
    visited[v] = False  # 訪問済みを解除する


dfs(0, 0)
print(ans)
