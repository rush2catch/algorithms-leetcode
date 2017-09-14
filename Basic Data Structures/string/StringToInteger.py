class Solution(object):
	def compareVersion(self, version1, version2):

		v1 = version1.split('.')
		v2 = version2.split('.')

		int_v1 = 0
		int_v2 = 0
		point_v1 = 0
		point_v2 = 0

		int_v1 = self.convert(v1[0])
		int_v2 = self.convert(v2[0])

		if len(v1) > 1:
			point_v1 = self.convert(v1[1])
		if len(v2) > 1:
			point_v2 = self.convert(v2[1])

		if int_v1 < int_v2:
			return -1
		elif int_v1 > int_v2:
			return 1
		else:
			if point_v1 < point_v2:
				return -1
			elif point_v1 > point_v2:
				return 1
			else:
				return 0

	def convert(self, s):
		if not s or len(s) == 0:
			return 0

		ans = 0
		n = len(s)
		table = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

		for i in range(n - 1, -1, -1):
			ans += table[s[i]] * (10**(n - 1 - i))

		return ans

obj = Solution()
s1 = '0.1'
s2 = '1.23'
s3 = '1.22'
print(obj.compareVersion(s2, s3))
