N, Q = map(int, input().split())
queries = []
for _ in range(Q):
    query = tuple(input().split())
    queries.append(query)

ans = []
should_care = "s"
# queriesを逆順にする
for query in queries[::-1]:
    if should_care == "s":
        if query[0] == '3':
            should_care = query[1]
    else:
        if query[1] == should_care:
            if query[0] == '1':
                should_care = "s"
            elif query[0] == '2':
                ans.append(query[2])

# ansを逆順にする
ans = ans[::-1]
print("".join(ans))