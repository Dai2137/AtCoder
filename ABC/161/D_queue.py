from collections import deque
K = int(input())

queue = deque(list(range(1,10)))

for k in range(K):
  k = queue.popleft()
  if k%10 != 0:
    queue.append(k*10 + k%10 - 1)
  queue.append(k*10 + k%10)
  if k%10 != 9:
    queue.append(k*10 + k%10 + 1)
  
print(k)
