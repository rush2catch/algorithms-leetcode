class Solution(object):
	def binary_search(self, nums, target):
		if len(nums) == 0:
			return None
		left = 0
		right = len(nums) - 1
		found = False
		while left <= right and not found:
			mid = round((left + right) / 2)
			if target == nums[mid]:
				pos = mid
				found = True
			if target < nums[mid]:
				right = mid - 1
			if target > nums[mid]:
				left = mid + 1
		if found:
			return found, pos
		else:
			return found, left

obj = Solution()
test1 = [0, 2, 5, 7, 9 ,11, 15]
test2 = []
test3 = [1, 3, 6 ,8, 10, 12]
print(obj.binary_search(test1, 9))
print(obj.binary_search(test1, 6))
print(obj.binary_search(test2, 10))
print(obj.binary_search(test3, 1))
print(obj.binary_search(test3, 13))