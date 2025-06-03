import math
N = int(input())

# エラトステネスの篩
# 素数列挙 (区間指定可)
def getPrimes(last: int, first: int = 1):
    # validation check
    if not isinstance(last, int) or \
        not isinstance(first, int):
        raise("[ERROR] parameter must be integer")
    if last < 0 or first < 0:
        raise("[ERROR] parameter must be not less than 0 (first >= 0 & last >= 0)")
    
    if last < first:
        last, first = first, last
    isPrime = [True] * (last + 1)    # 素数かどうか
    # 0と1をFalseに
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(last ** 0.5 + 1)):
        if isPrime[i]:
            # 篩にかける。iの倍数をすべてFalseにしていく。このとき i^2まではすでにふるい落とされているので見る必要がない
            for j in range(i ** 2, last + 1, i):
                isPrime[j] = False
    return [i for i in range(first, last + 1) if isPrime[i]] 

A = getPrimes(2000000)
cnt = 0
# a^8

# n = int(N ** (1 / 8))
# cnt = len(getPrimes(n))
# print(cnt)
# a^2 * b^2
for a in A:
    if a ** 8 > N:
        break
    cnt += 1


# n = int(N ** (1 / 2))

# for a in A:
#     if a ** 4 > N:
#         break
    # cnt += len(getPrimes(a + 1, math.floor(math.sqrt(N) / a) ))

for a in A:
    for b in A:
        if b >= a:
            break
        if a ** 2 * b ** 2 > N:
            break
        cnt += 1
                    
    
print(cnt)
