# Problem: Plus One
# Difficulty: Easy
# Category: Array/Math
# Leetcode 66: https://leetcode.com/problems/plus-one/#/description
# Description:
"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution(object):
    def plus_one(self, digits):
        """
        :param digits: List[int]
        :return: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits) - i - 1))

        return [int(i) for i in str(num + 1)]

obj = Solution()
print(obj.plus_one([2, 3, 4, 5]))
print(obj.plus_one([9, 9, 9, 9]))
