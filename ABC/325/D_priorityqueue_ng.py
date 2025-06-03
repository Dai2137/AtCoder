import heapq

N = int(input())

LR = []
lR = []
for i in range(N):
    L, D = map(int, input().split())
    R = L + D
    LR.append((L, R))
    lR.append(R)
LR.sort()

R_last = max(lR)

hp = []
heapq.heapify(hp)

t = 1
# ここまで考えられるべき商品の次の商品
item_next = 0 
# t_last = LR[]
ans = 0
while t <= R_last:
    if len(hp) == 0 and item_next < N:
        t = LR[item_next][0]
        # heapq.heappush(hp, LR[item_next][1])
    
    while hp and hp[0] < t:
        heapq.heappop(hp)
    
    while item_next < N and LR[item_next][0] == t:
        heapq.heappush(hp, LR[item_next][1])    
        item_next += 1
    
    if hp:
        heapq.heappop(hp)
        ans += 1
    # item_next -= 1
    t += 1    
print(ans)