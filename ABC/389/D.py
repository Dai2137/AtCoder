R = int(input())

# r = (R * 2) ** 2

# i = 1

# while r > (i**2) * 2:
#     i += 2

# r -= i ** 2

# if r < 1:
#     ans = (i - 2) ** 2
# else:
#     j = 1
#     while j**2 <= r:
#         j += 2
#     j -= 2

#     ans = i ** 2 - (((i - j) // 2 - 1) * 8 + 4 * (j != i))
# print(ans)
j = R
ans = 4*(R-1) + 1
for i in range(1,R+1):
    while (2*i + 1)**2 + (2*j + 1)**2 > 4 * (R ** 2):
        j-=1
        if j == 0:
            break
    if j==0:
        break
    ans += 4 * j
print(ans)
    