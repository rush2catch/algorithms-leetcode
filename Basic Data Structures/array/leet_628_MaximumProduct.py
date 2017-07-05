# Problem:  Maximum Product of 3 Numbers
# Difficulty: Easy
# Category: Array
# Leetcode 624: https://leetcode.com/problems/maximum-product-of-three-numbers/#/description
# Description:
"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.
Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""


class Solution(object):
	def maximum_product(self, nums):
		nums.sort()
		product1 = nums[-1] * nums[-2] * nums[-3]
		product2 = nums[0] * nums[1] * nums[-1]
		return max(product1, product2)

obj = Solution()
test_case1 = [1, 2, 3, 4]
test_case2 = [-8, -7, -6, 0, 1, 9]
test_case3 = [-4, -3, 0, 5]
test_case4 = [0, 3, 1, -5]
print(obj.maximum_product(test_case1))
print(obj.maximum_product(test_case2))
print(obj.maximum_product(test_case3))
print(obj.maximum_product(test_case4))
