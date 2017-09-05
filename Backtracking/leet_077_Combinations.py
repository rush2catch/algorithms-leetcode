# Problem: Combinations
# Difficulty: Medium
# Category: Backtracking
# Leetcode 77: https://leetcode.com/problems/combinations/description/
# Description:
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):

	def combine(self, n, k):
		if n <= 0 or n < k:
			return []
		nums = [i for i in range(1, n + 1)]
		ans = []
		temp = []
		self.backtrack(nums, temp, ans, k, 0)
		return ans

	def backtrack(self, nums, temp, res, k, start):
		if len(temp) == k:
			res.append([] + temp)
		else:
			for i in range(start, len(nums)):
				temp.append(nums[i])
				self.backtrack(nums, temp, res, k, i + 1)
				temp.pop()

obj = Solution()
print(obj.combine(3, 2))
