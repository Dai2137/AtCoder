N,M = map(int,input().split())
A=list(map(int,input().split()))

S=[0]*(N+1)
for i in range(N):
  S[i+1]=S[i]+A[i]

ans=0
cnt=[0]*M
cnt[0]=1
for r in range(1,N):
  ans+=cnt[S[r]%M]
  ans+=cnt[(S[r]-S[N])%M]
  cnt[S[r]%M]+=1
print(ans)











# from collections import defaultdict

# def count_pairs(N, M, distances):
#     # 累積和の初期値
#     cumulative_sum = 0
#     remainder_count = defaultdict(int)
#     remainder_count[0] = 1  # 開始点も考慮

#     # ペアの数
#     pair_count = 0
    
#     # 全体の円周の長さを計算
#     total_distance = sum(distances)
    
#     # 累積和を記録するリスト
#     cumulative_sums = [0]

#     for i in range(N-1):
#         # 累積和を計算
#         cumulative_sum += distances[i]
#         # cumulative_sums.append(cumulative_sum)
        
#         # 累積和を M で割った余り
#         # remainder = cumulative_sum % M
        
#         # その余りを持つ区間の数だけペアを増やす
#         pair_count += remainder_count[cumulative_sum % M]
#         pair_count += remainder_count[(cumulative_sum -total_distance)%M]
#         # 余りをカウント
#         remainder_count[cumulative_sum % M] += 1
    
#     # s > t の場合を考慮
#     # for i in range(1, N):
#     #     # 円周全体から累積和を引いた場合の余り
#     #     remainder = (total_distance - cumulative_sums[i]) % M
        
#     #     # その余りを持つ区間の数だけペアを増やす
#     #     pair_count += remainder_count[remainder]

#     return pair_count

# result = count_pairs(N, M, A)
# print(result)
