S = input()
nimotsu = []
for i in range(len(S)):
    if S[i] == "#":
        nimotsu.append(i + 1)

for i in range(0, len(nimotsu), 2):
    print(f"{nimotsu[i]},{nimotsu[i + 1]}")
