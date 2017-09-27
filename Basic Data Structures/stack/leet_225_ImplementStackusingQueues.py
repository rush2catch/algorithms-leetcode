# Problem:  Implement Stack using Queues
#  Difficulty: Easy
# Category: Stack
# Leetcode 225: https://leetcode.com/problems/implement-stack-using-queues/description/
# Description:
"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
"""


class MyStack(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.q1 = []
		self.q2 = []

	def push(self, x):
		"""
        Push element x onto stack.
		:type x: int
		:rtype: void
		"""

		self.q1.append(x)

	def pop(self):
		"""
		Removes the element on top of the stack and returns that element.
		:rtype: int
		"""
		for i in range(len(self.q1) - 1):
			self.q2.append(self.q1.pop(0))
		ans = self.q1.pop(0)
		for i in range(len(self.q2)):
			self.q1.append(self.q2.pop(0))
		return ans

	def top(self):
		"""
		Get the top element.
		:rtype: int
		"""
		if len(self.q1) == 0:
			return None
		else:
			return self.q1[-1]

	def empty(self):
		"""
		Returns whether the stack is empty.
		:rtype: bool
		"""
		return len(self.q1) == 0



#Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.top())
print(obj.empty())