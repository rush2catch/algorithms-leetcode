# Problem:  Shortest Unsorted Continuous Subarray
# Difficulty: Easy
# Category: Array
# Leetcode 581: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/#/description
# Description:
"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution(object):

	# a two - pointer solution:
	def find_subarray(self, nums):

		n = len(nums)
		end = -2
		begin = -1
		minVal = nums[n - 1]
		maxVal = nums[0]

		for i in range(1, n):
			minVal = min(minVal, nums[n - i - 1])
			maxVal = max(maxVal, nums[i])
			if nums[i] < maxVal:
				end = i
			if nums[n-i-1] > minVal:
				begin = n - i - 1

		return end - begin + 1



obj = Solution()
test_case1 = [2, 6, 4, 8, 10, 9, 15]
test_case2 = [1, 2, 3, 4, 5]
test_case3 = [1, 2, 4, 3, 5, 6]
test_case4 = [1, 3, 2, 3, 3]
print(obj.find_subarray(test_case1))
print(obj.find_subarray(test_case2))
print(obj.find_subarray(test_case3))
print(obj.find_subarray(test_case4))