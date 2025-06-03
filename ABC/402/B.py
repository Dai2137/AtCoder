from collections import deque
Q = int(input())
m = deque()
for _ in range(Q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        m.append(que[1])
    elif que[0] == 2:
        print(m.popleft())
  