T = int(input())


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    abs_set = set()
    for i in range(N):
        abs_set.add(abs(A[i]))
    if len(abs_set) == 1:
        if all(A[i] > 0 for i in range(N)) or all(A[i] < 0 for i in range(N)):
            print("Yes")
            return
        else:
            num_positive = 0
            num_negative = 0
            for i in range(N):
                if A[i] > 0:
                    num_positive += 1
                else:
                    num_negative += 1
            if num_positive - num_negative in [-1, 0, 1]:
                print("Yes")
                return
            else:
                print("No")
                return

    A_abs = [(abs(A[i]), A[i]) for i in range(N)]
    A_abs.sort()
    ans = True
    for i in range(1, N - 1):
        if A_abs[i][1] ** 2 != A_abs[i - 1][1] * A_abs[i + 1][1]:
            ans = False
            break
    # print(A_abs)
    if ans:
        print("Yes")
    else:
        print("No")

for _ in range(T):
    solve()
