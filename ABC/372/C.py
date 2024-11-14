N, Q = map(int,input().split())
S = list('..' + input() + '..')

cnt = 0

for i in range(N+2):
    cnt += S[i:i+3] == ['A', 'B', 'C']

for _ in range(Q):
    X,C = input().split()
    X = int(X) - 1 + 2
    for i in range(X-2, X+1):
        cnt -= S[i:i+3] == ['A', 'B', 'C']
    S[X] = C
    for i in range(X-2, X+1):
        cnt += S[i:i+3] == ['A', 'B', 'C']
    print(cnt)
