# Problem: 4 Sum
# Difficulty: Medium
# Category: Array
# Leetcode 18: https://leetcode.com/problems/4sum/description/
# Description:
"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.
Note: The solution set must not contain duplicate quadruplets.
For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
	def four_sum(self, nums, target):
		nums.sort()
		ans = []
		for i in range(len(nums) - 3):
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			target2 = target - nums[i]
			for j in range(i + 1, len(nums) - 2):
				if j > i + 1 and nums[j] == nums[j - 1]:
					continue
				left = j + 1
				right = len(nums) - 1
				while left < right:
					threeSum = nums[j] + nums[left] + nums[right]
					if threeSum < target2:
						left += 1
					elif threeSum > target2:
						right -= 1
					else:
						ans.append([nums[i], nums[j], nums[left], nums[right]])
						while left < right and nums[left] == nums[left + 1]:
							left += 1
						while left < right and nums[right] == nums[right - 1]:
							right -= 1
						left += 1
						right -= 1
		return ans

obj = Solution()
arr1 = [1, 0, -1, 0, -2, 2]
print(obj.four_sum(arr1, 0))
