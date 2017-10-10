# Problem: Maximum Subarray
# Difficulty: Easy
# Category: Array/DP
# Leetcode 53:https://leetcode.com/problems/maximum-subarray/description/
# Description:
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""


class Solution(object):
	def max_subarray(self, nums):
		currMax = totalMax = nums[0]
		for i in range(1, len(nums)):
			currMax = max(currMax + nums[i], nums[i])
			totalMax = max(currMax, totalMax)
		return totalMax

obj = Solution()
test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(obj.max_subarray(test1))