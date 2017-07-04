# Problem: Max Consecutive Ones
# Difficulty: Easy
# Category: Array
# Leetcode 485: https://leetcode.com/problems/max-consecutive-ones/#/description
# Description:
"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


class Solution(object):
	def find_max_consecutive_ones(self, nums):
		count = 0
		max_number = 0
		for i in range(len(nums)):
			if nums[i] == 1:
				count += 1
			else:
				if count > max_number:
					max_number = count
				count = 0

		return max(max_number, count)


obj = Solution()
test_case1 = [1, 1, 0, 1, 1, 1]
test_case2 = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
test_case3 = [0, 0, 0, 0]
print(obj.find_max_consecutive_ones(test_case1))
print(obj.find_max_consecutive_ones(test_case2))
print(obj.find_max_consecutive_ones(test_case3))