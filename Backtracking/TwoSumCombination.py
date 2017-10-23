# Description:
"""
Given a sorted list and a target number, find all the combinations of two numbers in the array that sum to the target.
for example:
[1, 1, 2, 4, 6, 8, 9, 9] -> [[1, 9], [1, 9], [1, 9], [1, 9], [2, 8], [4, 6]]
"""


class Solution(object):
	def two_sum(self, nums, target):
		if len(nums) < 2:
			return []
		ans = []
		temp = []
		self.dfs(nums, ans, temp, target, 0)
		return ans

	def dfs(self, nums, ans, temp, remain, start):
		if remain < 0:
			return
		elif remain == 0 and len(temp) == 2:
			ans.append([] + temp)
		else:
			for i in range(start, len(nums)):
				temp.append(nums[i])
				self.dfs(nums, ans, temp, remain - nums[i], i)
				temp.pop()

obj = Solution()
a1 = [1, 1, 2, 4, 6, 8, 9, 9]
a2 = [1, 2, 3, 4, 6, 7, 8, 9, 9]
print(obj.two_sum(a1, 10))
print(obj.two_sum(a2, 10))