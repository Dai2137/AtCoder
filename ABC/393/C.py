N, M = map(int, input().split())

simple = set()
for i in range(M):
    u, v = map(int, input().split())
    if u < v:
        simple.add((u, v))
    elif u > v:
        simple.add((v, u))

print(M - len(simple))
        