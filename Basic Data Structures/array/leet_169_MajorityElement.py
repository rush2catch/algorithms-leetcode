# Problem: Majority Element
# Difficulty: Easy
# Category: Array
# Leetcode 169: https://leetcode.com/problems/majority-element/#/description
# Description:
"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution(object):

	# sort the array, and the median is the majority element
	def find_majority_1(self, nums):
		if len(nums) == 0:
			return None
		if len(nums) == 1:
			return nums[0]
		if len(nums) == 2:
			if nums[0] == nums[1]:
				return nums[0]
			else:
				return None
		return sorted(nums)[int(len(nums) / 2)]

	# use a hash method
	def find_majority_2(self, nums):

		# corner case to determine whether the array is empty
		if len(nums) == 0:
			return None

		# initialize some params
		hash_buff = {}
		max_count = 0
		maj_num = 0

		# use a hash table to store the each element and the times it appears
		for i in range(len(nums)):
			if nums[i] in hash_buff:
				hash_buff[nums[i]] += 1
			else:
				hash_buff[nums[i]] = 1

		# find the majority one through the hash table
		for key in hash_buff:
			if hash_buff[key] > max_count:
				max_count = hash_buff[key]
				maj_num = key
		if max_count > int(len(nums)/2):
			return maj_num
		else:
			return None

testNums1 = [1, 1, 1, 1, 1, 1, 17]
testNums2 = [1, 2, 2, 3, 2, 4, 2]
testNums3 = [1, 2]
testNums5 = [3, 3, 4]
testNums4 = [2, 2]
obj = Solution()
print(obj.find_majority_1(testNums1))
print(obj.find_majority_1(testNums2))
print(obj.find_majority_1(testNums3))
print(obj.find_majority_1(testNums4))
print(obj.find_majority_1(testNums5))
print('-'*10)
print(obj.find_majority_2(testNums1))
print(obj.find_majority_2(testNums2))
print(obj.find_majority_2(testNums3))
print(obj.find_majority_2(testNums4))
print(obj.find_majority_2(testNums5))