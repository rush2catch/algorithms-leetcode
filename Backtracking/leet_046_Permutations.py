# Problem: Permutations
# Difficulty: Medium
# Category: Backtracking
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

	def permute(self, nums):
		if not nums:
			return []
		ans = []
		temp = []
		self.backtrack(nums, temp, ans)
		return ans

	def backtrack(self, nums, temp, ans):
		if len(temp) == len(nums):
			ans.append([] + temp)
		else:
			for i in range(len(nums)):
				if nums[i] in temp:
					continue
				temp.append(nums[i])
				self.backtrack(nums, temp, ans)
				temp.pop()


obj = Solution()
print(obj.permute([1, 2, 3]))