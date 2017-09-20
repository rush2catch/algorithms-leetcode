# Problem: 3 Sum Closest
# Difficulty: Medium
# Category: Array
# Leetcode 16: https://leetcode.com/problems/3sum-closest/description/
# Description:
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.
For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
	def three_sum(self, nums, target):
		if len(nums) == 0:
			return None
		minDiff = float('inf')
		result  = 0
		nums.sort()
		for i in range(len(nums) - 2):
			left = i + 1
			right = len(nums) - 1
			while left < right:
				sum3 = nums[i] + nums[left] + nums[right]
				if abs(sum3 - target) == 0:
					return summ
				elif abs(sum3 - target) < minDiff:
					minDiff = abs(sum3 - target)
					result = sum3
				if sum3 < target:
					left += 1
				if sum3 > target:
					right -= 1
		return result

obj = Solution()
print(obj.three_sum([-1, 2, 1, 4], 1))
