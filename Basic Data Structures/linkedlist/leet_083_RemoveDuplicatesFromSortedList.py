# Problem: Remove Duplicates from Sorted List
# Difficulty: Easy
# Category: Linked List
# Leetcode 83: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Description:
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


from node import *

class Solution(object):
	def remove_duplicates(self, head):
		if head is None or head.next is None:
			return head

		prev = head
		curr = head.next

		while curr:
			if curr.data != prev.data:
				prev.next = curr
				prev = curr
			curr = curr.next
		prev.next = None
		return head

obj = Solution()
n1 = Node(1)
n2 = Node(1)
n3 = Node(2)
n4 = Node(3)
n5 = Node(3)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(obj.remove_duplicates(n1).data, obj.remove_duplicates(n1).next.data, obj.remove_duplicates(n1).next.next.data, obj.remove_duplicates(n1).next.next.next)

