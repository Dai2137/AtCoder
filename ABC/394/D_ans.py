S = input()

former = ['(', '[', '<']
latter = [')', ']', '>']

dict = {'(': ')', '[': ']', '<': '>'}

N = len(S)
stack = []

i = 0
c = 0

for i in range(N):
    if S[i] in former:
        stack.append(dict[S[i]])
    else:
        if len(stack) == 0:
            print("No")
            exit()

        if S[i] != stack.pop():
            print("No")
            exit()

if len(stack) > 0:
    print("No")
else:
    print("Yes")
