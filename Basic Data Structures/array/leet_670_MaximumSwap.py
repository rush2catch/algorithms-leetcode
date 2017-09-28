# Problem: Maximum Swap
# Difficulty: Medium
# Category: Array
# Leetcode 670: https://leetcode.com/problems/maximum-swap/description/
"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
Return the maximum valued number you could get.
Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
"""


class Solution(object):


	def swap(self, n):
		if n == 0:
			return 0
		ans = 0
		nums = []
		while n != 0:
			tail = n % 10
			nums.insert(0, tail)
			n = n // 10
		arr = sorted(nums)
		self.reverse(arr)
		for i in range(len(nums)):
			if nums[i] == arr[i]:
				continue
			else:
				j = i + 1
				stop  = False
				maxDigits = 0
				while j < len(nums) and not stop:
					if nums[j] == arr[i]:
						maxDigits = arr[i]
						nums[i], nums[j] = nums[j], nums[i]
						stop = True
					j += 1
				break
		for i in range(len(nums) - 1, - 1, -1):
			ans += nums[i] * 10** (len(nums) - i -1)
		return ans

	def reverse(self, nums):
		if len(nums) == 0:
			return []
		left = 0
		right = len(nums) - 1
		while left  < right:
			nums[left], nums[right] = nums[right], nums[left]
			left += 1
			right -= 1
		return nums

obj = Solution()
print(obj.swap(2736), obj.swap(9973), obj.swap(1993))


