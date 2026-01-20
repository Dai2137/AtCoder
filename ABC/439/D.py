from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

ans = 0

num_to_idxlist = {}

for i in range(N):
    if A[i] not in num_to_idxlist:
        num_to_idxlist[A[i]] = []
    num_to_idxlist[A[i]].append(i)

for key, value in num_to_idxlist.items():
    value.sort()

for key, value in num_to_idxlist.items():
    if key % 5 != 0:
        continue
    Ai_cand = key // 5 * 7
    Ak_cand = key // 5 * 3
    if Ai_cand not in num_to_idxlist or Ak_cand not in num_to_idxlist:
        continue
    n_Ai_cand = len(num_to_idxlist[Ai_cand])
    n_Ak_cand = len(num_to_idxlist[Ak_cand])
    
    for j in value:
        n_Ai_cand_less_than_j = bisect_left(num_to_idxlist[Ai_cand], j)
        n_Ak_cand_less_than_j = bisect_left(num_to_idxlist[Ak_cand], j)
        ans += n_Ai_cand_less_than_j * n_Ak_cand_less_than_j + (n_Ai_cand - n_Ai_cand_less_than_j) * (n_Ak_cand - n_Ak_cand_less_than_j)
print(ans)