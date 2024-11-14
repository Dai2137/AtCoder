from collections import deque

Q = int(input())
que = deque()
height = [0] * (Q + 1)
for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        que.append(q + 1)
        height[q + 1] = height[q]
    elif query[0] == 2:
        T = query[1]
        height[q + 1] = height[q] + T
    elif query[0] == 3:
        H = query[1]
        count = 0
        while que:
            if height[q] - height[que[0]] >= H:
                que.popleft()
                count += 1
            else:
                break
        print(count)
        height[q + 1] = height[q]





















# from collections import deque

# q = int(input().strip())
# que = deque()
# height = [0] * (q + 1)

# for i in range(q):
#     query = list(map(int,input().split()))
    
#     if query[0] == 1:
#         height[i + 1] = height[i]
#         que.append(i)
    
#     elif query[0] == 2:
#         add = query[1]
#         height[i + 1] = height[i] + add
    
#     elif query[0] == 3:
#         height[i + 1] = height[i]
#         h = query[1]
#         ans = 0
        
#         while que:
#             if height[i + 1] - height[que[0]] >= h:
#                 ans += 1
#                 que.popleft()
#             else:
#                 break
          
#         print(ans)