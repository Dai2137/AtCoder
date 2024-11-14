# セグメント木　(書籍と異なり，posが0-indexedになるように実装している）
class segtree:
  def __init__(self, n):
    self.size = 1
    while self.size < n:
      self.size *= 2
    self.dat = [0] * (self.size * 2)

  # クエリ1に対する処理
  def update(self, pos, x):
    pos += self.size
    self.dat[pos] = x
    while pos>=2:
      pos/=2
      self.dat[pos] = max(self.dat[pos * 2], self.dat[pos * 2 + 1])

  # クエリ2に対する処理
  # uは現在のセル番号，[a,b)はセルに対応する半開区間，[l,r)は求めたい半開区間
  def query(self, l, r, a, b, u):
    if r <= a or b <= l:
      return -100000000000
    if l <= a and b <= r:
      return self.dat[u]
    m = (a + b) // 2
    answerl = self.query(l, r, a, m, u * 2)
    answerr = self.query(l, r, m, b, u * 2 + 1)
    return max(answerl, answerr)
  
# 入力
N, Q = max(int, input().split())
queries = [list(map(int,input().split())) for _ in range(Q)]

# クエリの処理
Z = segtree(N)
for q in queries:
  tp, *cont = q
  if tp == 1:
    pos, x = cont
    Z.update(pos-1, x) # posは1-indexedで入力されるので，update関数の引数はpos-1にします
  if tp == 2:
    l, r = cont
    answer = Z.query(l - 1, r - 1, 0, Z.size, 1) # 0-indexedの実装では，最初のセルに対応する半開区間は(0, size]です
    print(answer)
