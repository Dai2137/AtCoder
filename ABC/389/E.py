N, M = map(int, input().split())
P = list(map(int, input().split()))

ok = 0
ng = M + 1

def judge(c: int):
    tot = 0
    for i in range(N):
        tot += ((c // P[i] + 1) // 2 ) ** 2 * P[i]
    
    return tot <= M
    


while ok + 1 < ng:
    m = (ok + ng) // 2
    if judge(m):
        ok = m
    else:
        ng = m

ans = 0
for i in range(N):
    ans += int((ok / P[i] + 1) / 2 )

print(ans)







n, m = map(int, input().split())
p = list(map(int, input().split()))

def judge(c):
    global tot, num
    tot = 0
    num = 0
    for i in range(n):
        k = ((c - 1) // p[i] + 1) // 2
        if k <= 0:
            continue
        if m // (k * k * p[i]) == 0:
            return False
        tot += k * k * p[i]
        num += k
        if tot > m:
            return False
    return True

tot = 0
num = 0
ac = 1
wa = m + 1

while ac + 1 < wa:
    wj = (ac + wa) // 2
    if judge(wj):
        ac = wj
    else:
        wa = wj

judge(ac)
num += (m - tot) // ac
print(num)
