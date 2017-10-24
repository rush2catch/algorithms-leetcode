"""
Design and implement a TwoSum class. It should support the following operations: add
and find.
add(input) – Add the number input to an internal data structure.
find(value) – Find if there exists any pair of numbers which sum is equal to the value.
For example,
add(1); add(3); add(5); find(4)  true; find(7)  false
"""


class TwoSum(object):

	def __init__(self):
		self.nums = []

	def add(self, n):
		self.nums.append(n)

	def find(self, x):
		dic = {}
		if len(self.nums) == 0:
			return False
		for i in range(len(self.nums)):
			if x - self.nums[i] in dic:
				return True
			else:
				dic[self.nums[i]] = i
		return False

obj = TwoSum()
obj.add(1)
obj.add(3)
obj.add(5)
print(obj.find(4))
print(obj.find(7))
