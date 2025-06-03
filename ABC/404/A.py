import string

S = input()

for a in string.ascii_lowercase:
    if a not in S:
        print(a)
        exit()