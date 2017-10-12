# Problem: Next Permutation
# Difficulty: Medium
# Category: Array
# Leetcode 31: https://leetcode.com/problems/next-permutation/description/
# Description:
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):
	def next_permutation(self, nums):
		if len(nums) == 0:
			return []
		index = len(nums) - 2
		while index >= 0 and nums[index] >= nums[index + 1]:
			index -= 1
		if index >= 0:
			j = len(nums) - 1
			while j >= 0 and nums[j] <= nums[index]:
				j -= 1
			self.swap(nums, index, j)
		self.reverse(nums, index + 1)
		return nums

	def reverse(self, nums, index):
		left = index
		right = len(nums) - 1
		while left < right:
			nums[left], nums[right] = nums[right], nums[left]
			left += 1
			right -= 1

	def swap(self, nums, i, j):
		if len(nums) == 0:
			return
		nums[i], nums[j] = nums[j], nums[i]


obj = Solution()
arr1 = [1, 3, 2]
arr2 = [1, 5, 8, 4, 7, 6, 5, 3, 1]
print(obj.next_permutation(arr1), obj.next_permutation(arr2))
