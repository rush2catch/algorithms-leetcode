# Problem: Combination Sum II
# Difficulty: Medium
# Category: Array
# Leetcode 40: https://leetcode.com/problems/combination-sum/description/
# Description:
"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C only once.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7]
]
"""


class Solution(object):

	def combination(self, nums, target):
		if not nums:
			return []
		nums.sort()
		ans = []

		self.backtrack(ans, [], nums, target, 0)
		return ans

	def backtrack(self, ans, temp, nums, remain, start):
		if remain < 0:
			return
		elif remain == 0:
			ans.append([] + temp)
			return
		else:
			for i in range(start, len(nums)):
				if nums[i] in temp:
					continue
				temp.append(nums[i])
				self.backtrack(ans, temp, nums, remain - nums[i], i + 1)
				temp.pop()

obj = Solution()
nums = [2, 3, 6, 7]
target = 6
print(obj.combination(nums, target))
