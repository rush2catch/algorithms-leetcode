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


"""
We're given a list of digits, and the idea here is to convert that list to an integer, num.
So each digit is multiplied by the proper place value and added to num.
For example, if digits = [3, 8, 2, 5] then on the first iteration 3 is multiplied by 10 to the power of 4-1-0 = 3,
so this results in 3000, which is added to num. Then 8 is multiplied by 10^2 and added to num, and so on. 1

The last step is to add 1 to num, convert it to a list and return that list.
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

    def plus(self, digits):
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            summ = digits[i] + carry
            digits[i] = summ % 10
            carry  = summ // 10
        if carry == 1:
            digits.insert(0, 1)
        return digits



obj = Solution()
print(obj.plus([2, 3, 4, 5]))
print(obj.plus([9, 9, 9, 9]))
