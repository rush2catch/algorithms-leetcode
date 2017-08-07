# Problem: Linked List Cycle
# Difficulty: Easy
# Category: Linked List
# Leetcode 141: https://leetcode.com/problems/linked-list-cycle/description/
# Description:
"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


from node import *

class Solution(object):

	def has_cycle(self, head):
		if head is None or head.next is None:
			return False
		slow = head
		fast = head.next
		while fast and fast.next:
			if slow == fast:
				return True
			slow = slow.next
			fast = fast.next.next
		return False

obj = Solution()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n1
n4.next = n5
print(obj.has_cycle(n1))
print(obj.has_cycle(n4))

