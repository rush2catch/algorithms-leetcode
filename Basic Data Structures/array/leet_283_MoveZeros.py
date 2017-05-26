# Problem: Move Zeros
# Difficulty: Easy
# Category: Array/Two Pointers
# Leetcode 283: https://leetcode.com/problems/move-zeroes/#/description
# Description:
"""
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

# Solution:
"""
we use two pointers or commonly cursors: the headCur and the tailCur.
The headCur starts from the head of the array to find the zero element step by step.
The tailCur marked the end position of the HeadCur which is len(nums) - tailCur,
while tailCur is actually the count of zeros found by headCur.
Time Complexity: O(n)
"""


class Solution(object):
    def move_zeros(self, nums):
        if len(nums) < 2:
            return nums
        headCur = 0
        tailCur = 0
        while headCur < len(nums) - tailCur:
            if nums[headCur] == 0:
                nums.pop(headCur)
                nums.append(0)
                tailCur += 1
            else:
                headCur += 1
        return nums


obj = Solution()
print(obj.move_zeros([0, 0, 0, 1, 0, 3, 12]))
print(obj.move_zeros([0, 0, 1]))
