# Problem: Rotate Array
# Difficulty: Easy
# Category: Array
# Leetcode 189: https://leetcode.com/problems/rotate-array/#/description
# Description:
"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""


class Solution(object):

	# solution 1, use a stack to push and pop
	def rotate_array_1(self, nums, k):

		# corner case
		if len(nums) == 0:
			return None

		n = len(nums)
		k = k % n

		for i in range(k):
			nums.insert(0, nums.pop())

		return nums



obj = Solution()
testNums1 = [1, 2, 3, 4, 5, 6, 7]
testNums2 = []
print(obj.rotate_array_1(testNums1, 3))
print(obj.rotate_array_1(testNums2, 10))
print(obj.rotate_array_1(testNums1, 100))