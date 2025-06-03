import sys
from bisect import bisect_left

def chmax(x, y):
    return max(x, y)

def main():
    n, x = map(int, sys.stdin.readline().split())
    foods = [[] for _ in range(3)]
    
    for _ in range(n):
        v, a, c = map(int, sys.stdin.readline().split())
        v -= 1
        foods[v].append((a, c))
    
    d = [[0] * (x + 1) for _ in range(3)]
    
    for v in range(3):
        dp = [0] * (x + 1)
        for a, c in foods[v]:
            for i in range(x, c - 1, -1):
                dp[i] = chmax(dp[i], dp[i - c] + a)
        d[v] = dp[:]
    
    def judge(r):
        tot = 0
        for v in range(3):
            if d[v][x] < r:
                return False
            need = bisect_left(d[v], r)
            tot += need
        return tot <= x
    
    ac, wa = 0, 1001001001
    while ac + 1 < wa:
        wj = (ac + wa) // 2
        if judge(wj):
            ac = wj
        else:
            wa = wj
    
    print(ac)

if __name__ == "__main__":
    main()
