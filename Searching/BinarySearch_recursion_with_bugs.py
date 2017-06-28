class Solution(object):
	def binary_search(self, nums, target):

		if len(nums) == 0:
			return False

		# mid = round(len(nums) / 2)
		mid = len(nums) // 2
		if target == nums[mid]:
			return True
		if target > nums[mid]:
			return self.binary_search(nums[mid+1:], target)
		if target < nums[mid]:
			return self.binary_search(nums[:mid-1], target)

obj = Solution()
test1 = [0, 2, 5, 7, 9 ,11, 15]
test2 = []
test3 = [1, 3, 6 ,8, 10, 12]
print(obj.binary_search(test1, 9))
print(obj.binary_search(test1, 6))
print(obj.binary_search(test2, 10))
print(obj.binary_search(test3, 1))
print(obj.binary_search(test3, 13))
