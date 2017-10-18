# Problem: Add Two Numbers
# Difficulty: Medium
# Category: LinkedList
# Leetcode 2: https://leetcode.com/problems/add-two-numbers/description/
"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


class Solution(object):

	def add_two_numbers(self, l1, l2):
		if not l1 and not l2:
			return None
		carry = 0
		head = curr = ListNode(0)
		while l1 or l2:
			x = l1.val if l1 else 0
			y = l2.val if l2 else 0
			num = (x + y + carry) % 10
			carry = (x + y + carry) // 10
			curr.next = ListNode(num)
			curr = curr.next

			if l1:
				l1 = l1.next
			if l2:
				l2 = l2.next
		if carry == 1:
			curr.next = ListNode(1)
		return head.next
