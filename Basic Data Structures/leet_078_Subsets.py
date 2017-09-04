# Problem: Subsets
# Difficulty: Medium
# Category: Array
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
		self.dfs(ans, [], nums, 0)
		return ans

	def dfs(self, ans, temp, nums, start):
		if temp not in ans:
			ans.append([] + temp)
		for i in range(start, len(nums)):
			temp.append(nums[i])
			self.dfs(ans, temp, nums, i + 1)
			temp.pop()

obj = Solution()
nums1 = [1, 2, 3]
nums2 = [1, 2, 2]
print(obj.subset(nums2))