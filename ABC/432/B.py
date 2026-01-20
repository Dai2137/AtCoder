X = int(input())

nums = []
while X > 0:
    nums.append(X % 10)
    X //= 10

nums.sort()

for i in range(len(nums)):
    if nums[i] != 0:
        nums[i], nums[0] = nums[0], nums[i]
        break

print(int("".join(map(str, nums))))
