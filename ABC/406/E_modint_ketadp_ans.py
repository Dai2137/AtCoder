from atcoder.modint import Modint, ModContext

def solve_case(n: int, k: int) -> int:
    M = 60
    # n以下の問題をn+1未満の問題に変換
    n += 1

    # dp[bit][j][s][p]
    # dp[i][j][s][p]
    # i: 今見ているビット位置（上位から）
    # j:既に◯をつけたか． 先頭の1が出たか？（0=出てない, 1=出た）
    # s: N未満であることが確定してるか？（0=一致中, 1=小さい）
    # p: popcount（今までに置いた1の数）
    # dpの要素は個数ではなく総和

    dp = [[[[Modint(0) for _ in range(k + 1)] for _ in range(2)] for _ in range(2)] for _ in range(M + 1)]
    dp[M][0][0][0] = Modint(1)

    for i in range(M - 1, -1, -1):
        for j in range(2):
            for s in range(2):
                for p in range(k + 1):
                    now = dp[i + 1][j][s][p]
                    if now.val() == 0:
                    # if now == 0:
                        continue
                    for a in range(2): #i桁目に置く数字
                        ns, np = s, p + a
                        if s == 0:
                            # nの下からi桁目
                            bit = (n >> i) & 1
                            if a < bit:
                                ns = 1 #N未満であることが確定
                            elif a > bit:
                                continue #Nを超えるので無効
                        if np > k:
                            continue
                        dp[i][j][ns][np] += now #個数の更新
                        if j == 0 and a == 1:
                            dp[i][1][ns][np] += now * (1 << i)
    
    return dp[0][1][1][k].val()

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    T = int(input())
    with ModContext(998244353):
        for _ in range(T):
            n, k = map(int, input().split())
            print(solve_case(n, k))
