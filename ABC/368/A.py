N,K=map(int,input().split())
A=list(map(int,input().split()))
ans=A[N-K:]+A[:N-K]
print(*ans)