# Problem: Permutations
# Difficulty: Medium
# Category: Backtracking
# Leetcode 47: https://leetcode.com/problems/permutations-ii/description/
# Description:
"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):

	def permute(self, nums):
		if len(nums) == 0:
			return []
		ans = []
		temp = []
		self.dfs(nums, ans, temp)
		return ans

	def dfs(self, nums, ans, temp):
		if len(temp) == len(nums):
			ans.append([] + temp)
		else:
			for i in range(len(nums)):
				if nums[i] in temp:
					continue
				temp.append(nums[i])
				self.dfs(nums, ans, temp)
				temp.pop()

obj = Solution()
a1 = [1, 1, 2]
print(obj.permute(a1))