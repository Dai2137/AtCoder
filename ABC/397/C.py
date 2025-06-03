N = int(input())
A = list(map(int, input().split()))

ans = len(set(A))
dict = {}

for i in range(N):
    if A[i] not in dict:
        dict[A[i]] = []
    dict[A[i]].append(i)

events = []
for key in dict:
    m = dict[key][0]
    M = dict[key][-1]
    if m != M:
        events.append((m, 1))
        events.append((M, -1))

events.sort()
cnt = ans

for i, change in events:
    cnt += change
    if cnt > ans:
        ans = cnt
# print(events)

print(ans)    
    