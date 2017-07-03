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

		# initialize
		sorted_array = sorted(nums)
		left_stop = False
		right_stop = False
		left = 0
		right = len(nums) - 1

		print(nums)
		print(sorted_array)

		# use two pointers moving from start and end to locate
		while left <= right and (not left_stop or not right_stop):

			while not left_stop:

				if nums[left] != sorted_array[left]:
					left_stop = True
				else:
					left += 1
				print("left: {}, left_stop: {}".format(left, left_stop))

			while not right_stop:
				if nums[right] != sorted_array[right]:
					right_stop = True
				else:
					right -= 1
				print("right: {}, right_stop: {}".format(right, right_stop))

		return right - left + 1

obj = Solution()
test_case1 = [2, 6, 4, 8, 10, 9, 15]
test_case2 = [1, 2, 3, 3, 4, 5]
print(obj.find_subarray(test_case1))
print(obj.find_subarray(test_case2))