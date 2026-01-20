N = int(input())
A = list(map(int, input().split()))

stack= []
for i in range(N):
    if not stack or stack[-1][0] != A[i]:
        stack.append([A[i], 1])
    else:
        stack[-1][1] += 1
    if stack[-1][1] == 4:
        stack.pop()
    # print(stack)
ans = 0
for i in range(len(stack)):
    ans += stack[i][1]
print(ans)