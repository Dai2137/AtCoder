# N, M = map(int, input().split())

# G = [[]] * N
# for i in range(M):
#     u, v, w = map(int, input().split())
#     u -= 1
#     v -= 1
#     G[u].append((v, w))
#     G[v].append((u, w))

# def dfs(node, visited, path, ans, xor):
#     visited.add(node)
#     path.append(node)
    
#     if node == N - 1:
#         ans = min(ans, xor)
#     else:
#         for neighbor, weight in G[node]:
#             if neighbor not in visited:
#                 dfs(neighbor, visited, path, ans, xor ^ weight)
    
#     path.pop()
#     visited.remove(node)
    
# visited = set([])
# ans = 10 ** 10
# dfs(0, visited, [], ans, 0)

# print(ans)
# print(visited)

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))

def dfs(node, visited, xor):
    if node == N - 1:
        return xor  # 終点に着いたら XOR 値を返す

    visited.add(node)
    min_xor = float('inf')

    for neighbor, weight in G[node]:
        if neighbor not in visited:
            min_xor = min(min_xor, dfs(neighbor, visited, xor ^ weight))

    visited.remove(node)
    return min_xor

visited = set()
ans = dfs(0, visited, 0)

print(ans)
