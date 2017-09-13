# Problem:   Third Maximum Number
# Difficulty: Easy
# Category: Array
# Leetcode 414: https://leetcode.com/problems/third-maximum-number/description/
# Description:
"""
Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).
"""


class Solution(object):

	def third_max(self, nums):
		max1 = None
		max2 = None
		max3 = None

		for n in nums:
			if n == max1 or n == max2 or n == max3:
				continue
			if  max1 is None or n > max1:
				max3 = max2
				max2 = max1
				max1 = n
			elif max2 is None or n > max2:
				max3 = max2
				max2 = n
			elif max3 is None or n > max3:
				max3 = n
			else:
				continue

		if max3 is None:
			return max1
		else:
			return max3

obj = Solution()
t1 = [3, 2, 1]
t2 = [1, 2]
t3 = [3, 2, 2, 1]
t4 = [-2147483648, -2147483648, -2147483648, -2147483648, 1, 1, 1]
#print(obj.third_max(t1), obj.third_max(t2), obj.third_max(t3))
print(obj.third_max(t4))
