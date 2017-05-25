def two_sum(nums, target):
    ans = ['null', 'null']

    for i in range(len(nums)):
        temp = target - nums[i]
        for j in range(i, len(nums)):
            if temp == nums[j]:
                ans[0] = i
                ans[1] = j

    return ans

nums_0 = [2, 7, 11, 15]
nums_1 = [34, 56, 23, 45, 2, 44, 12, 21]
print(two_sum(nums_0, 9))
print(two_sum(nums_0, 8))
print(two_sum(nums_0, 26))
print(two_sum(nums_1, 47))