import string

T = list(input())
U = input()

Ts = []
hatena_idxs = []

for i in range(len(T)):
    if T[i] == "?":
        hatena_idxs.append(i)

for a in string.ascii_lowercase:
    # c に 'a', 'b', 'c', …, 'z' が順に入る
    for b in string.ascii_lowercase:
        for c in string.ascii_lowercase:
            for d in string.ascii_lowercase:
                T_copy = T.copy()
                T_copy[hatena_idxs[0]] = a
                T_copy[hatena_idxs[1]] = b
                T_copy[hatena_idxs[2]] = c
                T_copy[hatena_idxs[3]] = d
                T_copy = "".join(T_copy)
                Ts.append(T_copy)

ans = False
for S in Ts:
    if U in S:
        ans = True
        break
print("Yes" if ans else "No")