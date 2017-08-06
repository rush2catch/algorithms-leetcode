import math

class Solution(object):
	def find_prime(self):
		count = 1
		primes = [2]
		for num in range(3, 100, 1):
			stop = False
			sqrt = round(math.sqrt(num))
			i = 2
			while 2 <= i <= sqrt and not stop:
				if num % i == 0:
					stop = True
				i += 1
			if not stop:
				count += 1
				primes.append(num)
		return primes, count, sum(primes)

obj = Solution()
print(obj.find_prime())