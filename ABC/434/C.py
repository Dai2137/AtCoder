T = int(input())

def solve():
    N, H = map(int, input().split())
    t,l,u = [], [], []
    for _ in range(N):
        t_, l_, u_ = map(int, input().split())
        t.append(t_)
        l.append(l_)
        u.append(u_)
    tnow = 0
    Hnow_range = (H, H)
    for i in range(N):
        can_range = (Hnow_range[0] - (t[i] - tnow), Hnow_range[1] + (t[i] - tnow))
        if max(l[i], can_range[0]) <= min(u[i], can_range[1]):
            Hnow_range = (max(l[i], can_range[0]), min(u[i], can_range[1]))
            tnow = t[i]
            
        else:
            print("No")
            return
    print("Yes")
    


for _ in range(T):
    solve()
