# Problem: Subsets
# Difficulty: Medium
# Category: Backtracking
# Leetcode 78: https://leetcode.com/problems/subsets/description/
# Description:
"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):

	def subset(self, nums):
		if not nums:
			return []

		ans = []
		temp = []
		self.backtrack(nums, temp, ans, 0)
		return ans

	def backtrack(self, nums, temp, ans, start):
		ans.append([] + temp)
		for i in range(start, len(nums)):
			temp.append(nums[i])
			self.backtrack(nums, temp, ans, i + 1)
			temp.pop()

obj = Solution()
print(obj.subset([1, 2, 3]))