N, Q = map(int, input().split())

p2b = list(range(N))
b2l = list(range(N))
l2b = list(range(N))


for _ in range(Q):
    t, a, *b = map(int, input().split())    
    a -= 1  # 0-index に変換
    
    match t:
        case 1:
            # t=1 のときの処理
            b = b[0] - 1  # 0-index に変換
            p2b[a] = l2b[b]

        case 2:
            # t=2 のときの処理（グループ a と b を交換）
            b = b[0] - 1  # 0-index に変換
            l2b[a], l2b[b] = l2b[b], l2b[a]
            b2l[l2b[a]] = a
            b2l[l2b[b]] = b
            

        case _:
            # t!=1 and t!=2 のとき（a の現在のグループを出力）
            print(b2l[p2b[a]] + 1)
