# Problem: Can Place Flowers
# Difficulty: Easy
# Category: Array
# Leetcode 605: https://leetcode.com/problems/can-place-flowers/#/description
# Description:
"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not.
However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty),
and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""


class Solution(object):

	def can_place_flowers(self, flowerbed, n):
		"""

        :param flowerbed: List[int]
        :param n: int
        :return: book
        """

		# corner case
		if n == 0:
			return True
		if len(flowerbed) == 0:
			return False
		if len(flowerbed) == 1:
			if flowerbed[0] == 0:
				return True
			else:
				return False

		# initialize
		pos = []
		count_zero = 0
		bed_length = len(flowerbed)
		k = 0

		# find the positions of 1 in the flowerbed
		for i in range(len(flowerbed)):
				if flowerbed[i] == 1:
					pos.append(i)
		# print(pos)
		# print(bed_length)

		# calculate the number of zeros between two adjacent 1s
		if len(pos) == 0:
			count_zero = int((bed_length + 1) / 2)
		while 0 <= k <= len(pos) - 1:
			if k == 0:
				if len(pos) == 1:
					count_zero += int(pos[k] / 2)
					count_zero += int((bed_length - 1 - pos[k]) / 2)
				else:
					count_zero += int(pos[k] / 2)
				# print("1 -- k= {}, count_zero={} ".format(k, count_zero))
			elif k == len(pos) - 1:
				count_zero += int((bed_length - 1 - pos[k]) / 2)
				count_zero += int((pos[k] - pos[k - 1] - 1 - 1) / 2)
				# print("2 -- k= {}, count_zero={} ".format(k, count_zero))
			elif 0 < k < len(pos) - 1:
				count_zero += int((pos[k] - pos[k - 1] - 1 - 1) / 2)
				# print("3 -- k= {}, count_zero={} ".format(k, count_zero))

			k += 1

		if count_zero < n:
			return False
		else:
			return True

	# method 2: same as 1, but with much cleaner code
	def place_flowers(self, flowerbed, n):

		count = 1
		result = 0

		for i in range(len(flowerbed)):
			if flowerbed[i] == 0:
				count += 1
			else:
				result += int((count - 1) / 2)
				count = 0

		if count != 0:
			result += int(count / 2)

		return result >= n

obj = Solution()
flowerbed1 = [1, 0, 0, 0, 1]
flowerbed2 = [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
flowerbed3 = [0, 0, 1, 0, 0]
flowerbed4 = [1]
flowerbed5 = [0, 0, 0, 0, 0]
print(obj.can_place_flowers(flowerbed1, 1), end=' ')
print(obj.can_place_flowers(flowerbed1, 2), end=' ')
print(obj.can_place_flowers(flowerbed2, 4), end=' ')
print(obj.can_place_flowers(flowerbed2, 5), end=' ')
print(obj.can_place_flowers(flowerbed3, 2), end=' ')
print(obj.can_place_flowers(flowerbed4, 0), end=' ')
print(obj.can_place_flowers(flowerbed5, 3))

print(obj.place_flowers(flowerbed1, 1), end=' ')
print(obj.place_flowers(flowerbed1, 2), end=' ')
print(obj.place_flowers(flowerbed2, 4), end=' ')
print(obj.place_flowers(flowerbed2, 5), end=' ')
print(obj.place_flowers(flowerbed3, 2), end=' ')
print(obj.place_flowers(flowerbed4, 0), end=' ')
print(obj.place_flowers(flowerbed5, 3))
