from collections import deque
N = int(input()) + 2
S = input() + ".."
T = input() + ".."

ans = -1

que = deque([S])
cnt = {S: 0}

while que:
    s = que.popleft()
    if s == T:
        ans = cnt[s]
    
    empty = s.find('..')
    for i in range(N-1):
        if '.' not in s[i:i+2]:
            ls = list(s)
            ls[empty : empty + 2] = ls[i : i + 2]
            ls[i : i + 2] = ['.', '.']
            ls = "".join(ls)
            if ls not in cnt:
                cnt[ls] = cnt[s] + 1
                que.append(ls)

print(ans)
