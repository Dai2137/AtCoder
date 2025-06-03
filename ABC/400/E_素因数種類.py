from bisect import bisect_right
import math
Q = int(input())

prime_unique = [0] * 1000001
for i in range(2, 1000001):
    if prime_unique[i] == 0:
        for j in range(i, 1000001, i):
            prime_unique[j] += 1

is_400n = []
for i in range(2, 1000001):
    if prime_unique[i] == 2:
        is_400n.append(i ** 2)

# is_400n = []
# for i in range(1, 1000001):
#     if has_2prime[i]:
#         is_400n.append(i ** 2)
        
for _ in range(Q):
    A = int(input())
    print(is_400n[bisect_right(is_400n, A) - 1])
    
    
    
    
    
    