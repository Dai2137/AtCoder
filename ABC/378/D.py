# from collections import deque

H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
didj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(i: int, j: int, visited=None, path_count=0) -> None:
    global ans  # グローバル変数 ans を使用することを明示
    if path_count == K:  # 指定されたパスの長さに到達した場合
        ans += 1
        return

    if visited is None:  # 訪問済みノードの初期化
        visited = set()

    visited.add((i, j))  # 現在のノードを訪問済みとして追加

    for di, dj in didj:
        ni, nj = i + di, j + dj
        # 境界チェックと未訪問チェック
        if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == '.' and (ni, nj) not in visited:
            # 再帰呼び出しの前に visited のコピーを渡す
            dfs(ni, nj, visited.copy(), path_count + 1) 

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':  # 開始地点が通行可能な場合のみ探索
            dfs(i, j)  # 各セルを開始点として DFS を実行

print(ans)
