# Problem: Permutations
# Difficulty: Medium
# Category: Array
# Leetcode 46: https://leetcode.com/problems/permutations/description/
# Description:
"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):

	def permutation(self, nums):
		if not nums:
			return []
		nums.sort()
		ans = []
		self.dfs(nums, ans, [])
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
nums = [1, 3, 2]
print(obj.permutation(nums))
