class Solution(object):

	def dedup(self, nums):
		if len(nums) == 0:
			return 0

		low = 0
		high = 0
		count = 0
		n = len(nums)

		while high < n:
			if nums[high] == nums[low]:
				count += 1
				if count > 2:
					nums.pop(high)
					n -= 1
					count -= 1
				else:
					high += 1
			else:
				low = high
				count = 0

		return nums

obj = Solution()
arr1 = [1, 1, 1, 2, 2, 3]
print(obj.dedup(arr1))
