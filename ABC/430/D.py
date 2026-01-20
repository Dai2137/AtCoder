# from bisect import bisect_left
from sortedcontainers import SortedList
N = int(input())
X = [0] + list(map(int, input().split()))

INF = 10 ** 18
ans = INF
already_man = SortedList([0]) # 座標

X_to_dist = {0: INF}

for r in range(1, N + 1):
    pos = X[r]
    i = already_man.bisect_left(pos)
    already_man.add(pos)
    # i - 1の変更
    if i - 1 >= 0:
        ans -= X_to_dist[already_man[i - 1]]
        X_to_dist[already_man[i - 1]] = min(X_to_dist[already_man[i - 1]], pos - already_man[i - 1])
        ans += X_to_dist[already_man[i - 1]]
    # i + 1の変更
    if i < r:
        ans -= X_to_dist[already_man[i + 1]]
        X_to_dist[already_man[i + 1]] = min(X_to_dist[already_man[i + 1]], already_man[i + 1] - pos)
        ans += X_to_dist[already_man[i + 1]]
    
    # iの変更
    if i == 0:
        X_to_dist[pos] = already_man[i + 1] - pos
    elif i == r:
        X_to_dist[pos] = pos - already_man[i - 1]
    else:
        X_to_dist[pos] = min(pos - already_man[i - 1], already_man[i + 1] - pos)
    ans += X_to_dist[pos]
    
    print(ans)
        
    
