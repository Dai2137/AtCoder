M=int(input())
# A = list(map(int,input().split()))

def decimal_to_ternary(n):
    if n == 0:
        return '0'
    ternary = ''
    while n > 0:
        ternary = str(n % 3) + ternary
        n //= 3
    return ternary

M3 = decimal_to_ternary(M)
A = []
for i in range(len(M3)):
    A += [i] * int(M3[len(M3)-1-i])

print(len(A))
print(*A)