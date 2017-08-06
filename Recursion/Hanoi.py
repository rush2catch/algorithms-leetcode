
class Solution(object):
	def hanoi(self, n):
		fp = 'C'
		tp = 'A'
		wp = 'B'
		self.moveTower(n, fp, tp, wp)

	def moveTower(self,height, fromPole, toPole, withPole):
		if height >= 1:
			self.moveTower(height - 1, fromPole, withPole, toPole)
			self.printRoute(fromPole, toPole)
			self.moveTower(height - 1, withPole, toPole, fromPole)

	def printRoute(self, fromPole, toPole):
		print(fromPole, "->", toPole)

obj = Solution()
obj.hanoi(0)
print('-'*20)
obj.hanoi(1)
print('-'*20)
obj.hanoi(2)
print('-'*20)
obj.hanoi(3)