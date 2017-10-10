# Problem: Merge Two Sorted Lists
# Difficulty: Easy
# Category: LinkedList
# Leetcode 014: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Description:
"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
	def mergeTwoLists(self, l1, l2):
		head = curr = ListNode(0)

		while l1 and l2:
			if l1.val < l2.val:
				curr.next = l1
				l1 = l1.next
			else:
				curr.next = l2
				l2 = l2.next
			curr = curr.next

		if l1.next == None:
			curr.next = l2
		else:
			curr.next = l1

		return head.next

