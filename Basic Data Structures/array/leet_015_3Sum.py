# Problem: 3 Sum
# Difficulty: Medium
# Category: Array
# Leetcode 15: https://leetcode.com/problems/3sum/description/
# Description:
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
	def three_sum(self, nums):
		if not nums:
			return []
		nums.sort()
		ans = []
		for i in range(len(nums) - 2):
			if i > 0 and nums[i] == nums[i-1]:
				continue
			left = i + 1
			right = len(nums) - 1
			while left < right:
				sum3 = nums[i] + nums[left] + nums[right]
				if sum3 > 0:
					right -= 1
				elif sum3 < 0:
					left += 1
				else:
					ans.append([nums[i], nums[left], nums[right]])
					while left < right and nums[left] == nums[left + 1]:
						left += 1
					while left < right and nums[right] == nums[right - 1]:
						right -= 1
					left += 1
					right -= 1
		return ans

obj = Solution()
arr1 = [-1, 0, 1, 2, -1, -4]
arr2 = [-1, -1, -1, 0, 0, 0, 1, 1]
print(obj.three_sum(arr1), obj.three_sum(arr2))