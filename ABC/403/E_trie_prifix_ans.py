import sys
sys.setrecursionlimit(10**7)


input = sys.stdin.readline
q = int(input())

class Trie:
    def __init__(self):
        # トライの子への遷移: to[v] は dict で {char: next_index}
        self.to = [{}]
        self.ans = 0
        self.ng = []
        self.num_y = []

    def add(self, s: str) -> int:
        """
        文字列 s をトライに追加し，末端のノード番号を返す
        """
        v = 0    # 現在のノード番号（整数）
        for c in s:         
            if c not in self.to[v]:
                self.to[v][c] = len(self.to)
                self.to.append({})
            v = self.to[v][c]
        return v

    def init(self):
        """
        クエリ処理前の初期化
        ng: 削除フラグ
        num_y: 各ノードに対する addy の回数
        ans: 現在の有効ノード数
        """
        n = len(self.to)
        self.ng = [False] * n
        self.num_y = [0] * n
        self.ans = 0

    def addx(self, v: int):
        """
        type=1 クエリ: ノード v 以下をすべて削除
        """
        if self.ng[v]:
            return
        self.ng[v] = True
        self.ans -= self.num_y[v]
        for u in self.to[v].values():
            self.addx(u)

    def addy(self, v: int):
        """
        type=2 クエリ: ノード v にマーク
        """
        if self.ng[v]:
            return
        self.ans += 1
        self.num_y[v] += 1

# トライ構築とクエリバッファリング
t = Trie()
qs: list[tuple[int,int]] = []
for _ in range(q):
    typ, s = input().split()
    typ = int(typ)
    v = t.add(s.strip())
    qs.append((typ, v))

# 初期化してからクエリ実行
t.init()
out = []
for typ, v in qs:
    if typ == 1:
        t.addx(v)
    else:
        t.addy(v)
    out.append(str(t.ans))

# 結果出力
sys.stdout.write("\n".join(out))

