# Problem: Product of Array Except Self
# Difficulty: Medium
# Category: Array
# Leetcode 238: https://leetcode.com/problems/product-of-array-except-self/description/
# Description:
"""
Given an array of n integers where n > 1, nums,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Solve it without division and in O(n).
For example, given [1,2,3,4], return [24,12,8,6].
Follow up:
Could you solve it with constant space complexity?
(Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution(object):
	def product_except_self(self, nums):
		factor = 1
		ans = []
		for i in range(len(nums)):
			ans.append(factor)
			factor *= nums[i]
		factor = 1
		for i in range(len(nums) - 1, -1, -1):
			ans[i] *= factor
			factor *= nums[i]
		return ans

obj = Solution()
arr1 = [1, 2, 3, 4]
arr2 = [2, 3, 5, 7]
arr3 = [3, 6, 2, 8]
print(obj.product_except_self(arr1), obj.product_except_self(arr2), obj.product_except_self(arr3))
