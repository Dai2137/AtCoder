from collections import deque  # BFS に使用する deque をインポート

# 頂点数 n, 辺数 m を入力
n, m = map(int, input().split())

# 隣接リスト g を作成（頂点ごとに (隣接頂点, 辺の重み) を格納）
g = [[] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    x, y = x - 1, y - 1  # 0-indexed に変換
    g[x].append((y, z))
    g[y].append((x, z))

# 各頂点の訪問状態を管理するリスト
visited = [False] * n

# 各頂点の XOR 値（val[i] は i 番目の頂点の値）
val = [-1] * n  # 未確定な値を -1 で初期化

def bfs(start):
    """
    幅優先探索（BFS）を用いて、各連結成分を探索し、
    頂点ごとの XOR 値を求める。
    """
    dq = deque([start])  # BFS のためのキュー
    visited[start] = True  # 開始ノードを訪問済みにする
    comp = [start]  # 連結成分に含まれる頂点を記録
    while dq:
        v = dq.popleft()  # キューの先頭を取り出す
        for u, w in g[v]:  # 頂点 v からの辺を探索
            if not visited[u]:  # まだ訪問していない場合
                visited[u] = True
                val[u] = val[v] ^ w  # XOR を使って u の値を決定
                comp.append(u)
                dq.append(u)
            else:
                # すでに訪問済みの u に矛盾がある場合は -1 を出力して終了
                if val[u] != val[v] ^ w:
                    print("-1")
                    exit()
    return comp  # 連結成分の頂点リストを返す

# 以下，最適化

# 各頂点の最終的な値を格納するリスト
ans = [0] * n

# すべての頂点を探索し、未訪問の連結成分ごとに処理
for st in range(n):
    if visited[st]:  # すでに訪問済みならスキップ
        continue
    val[st] = 0  # 連結成分の最初の頂点を 0 に設定
    comp = bfs(st)  # BFS で連結成分を取得

    # 各ビットごとに、値の調整を行う
    for i in range(30):  # 30 ビット分（辺の重みの最大ビット数を想定）
        cnt = 0  # 1 のビットが立っている頂点のカウント
        for j in comp:
            if val[j] & (1 << i):  # i ビット目が 1 であるか判定
                cnt += 1

        # より多い方を 0 にする（多数派の値に合わせることで XOR の最適化）
        if cnt < len(comp) - cnt:
            for j in comp:
                if val[j] & (1 << i):
                    ans[j] |= 1 << i
        else:
            for j in comp:
                if not (val[j] & (1 << i)):
                    ans[j] |= 1 << i

# 最終的な各頂点の値を出力
print(*ans)
