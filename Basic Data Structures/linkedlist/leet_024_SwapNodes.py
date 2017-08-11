# Problem: Swap Nodes in Pairs
# Difficulty: Medium
# Category: Linked List
# Leetcode 24: https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Description:
"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""


from node import *

class Solution(object):

	def swap_pairs(self, head):

		if head is None or head.next is None:
			return head

		dummy = Node(0)
		dummy.next = head
		prev = dummy

		while prev.next is not None and prev.next.next is not None:
			curr = prev.next
			front = prev.next.next
			curr.next = front.next
			prev.next = front
			prev.next.next = curr
			prev = prev.next.next

		return dummy.next

obj = Solution()
n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = None
print(obj.swap_pairs(n1))
print(n2)
print(obj.swap_pairs(n1).next)
print(n1)
print(obj.swap_pairs(n1).next.next)
print(n4)
print(obj.swap_pairs(n1).next.next.next)
print(n3)
"""
print(obj.swap_pairs(n1).data)
print(obj.swap_pairs(n1).next.data)
print(obj.swap_pairs(n1).next.next.data)
print(obj.swap_pairs(n1).next.next.next.data)
print(obj.swap_pairs(n1).next.next.next.next.data)
"""