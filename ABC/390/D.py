import sys

n = int(input())
a = list(map(int, input().split()))

xs = set()
def dfs(i, groups):
    if i == n:
        xor = 0
        for group in groups:
            sum = 0
            for stone in group:
                sum += stone
            xor ^= sum
        xs.add(xor)
        return
    
    for group in groups:
        group.append(a[i])
        dfs(i + 1, groups)
        group.pop()
    
    groups.append([a[i]])
    dfs(i + 1, groups)
    groups.pop()
    
dfs(0, [])

print(len(xs))