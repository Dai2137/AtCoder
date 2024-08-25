N,K=map(int,input().split())
R=list(map(int,input().split()))

def f(i,A):
  if i==N:
    if sum(A)%K==0:
      print(*A)
  
  else:
    for j in range(1,R[i]+1):
      A.append(j)
      f(i+1,A)
      A.pop()

f(0,[])


# from itertools import product

# def enumerate_lists(R):
#     # 各 Ri に対して 1 以上 Ri 以下のリストを生成
#     ranges = [range(1, Ri + 1) for Ri in R]
    
#     # すべての組み合わせを生成
#     all_combinations = list(product(*ranges))
    
#     return all_combinations

# result = enumerate_lists(R)
# for combination in result:
#     if sum(combination)%K==0:
#        print(*combination)


