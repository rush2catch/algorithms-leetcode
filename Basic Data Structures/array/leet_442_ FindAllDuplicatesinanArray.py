# Problem:  Find All Duplicates in an Array
# Difficulty: Medium
# Category: Array
# Leetcode 442: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# Description:
"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]
"""


class Solution(object):

	def find_dup(self, nums):
		i = 0
		ans = []
		n = len(nums)
		while i < n:
			if nums[i] == 0:
				i += 1
			elif nums[i] == i + 1:
				i += 1
			else:
				if nums[i] == nums[nums[i] - 1]:
					ans.append(nums[i])
					nums[i] = 0
					i += 1
				else:
					temp = nums[i]
					nums[i] = nums[temp - 1]
					nums[temp - 1] = temp

		return ans

obj = Solution()
t1 = [4, 3, 2, 7, 8, 2, 3, 1]
print(obj.find_dup(t1))