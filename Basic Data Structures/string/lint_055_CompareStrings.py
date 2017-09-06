"""
比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母
在 A 中出现的 B 字符串里的字符不需要连续或者有序。
给出 A = "ABCD" B = "ACD"，返回 true
给出 A = "ABCD" B = "AABC"， 返回 false
"""


class Solution(object):

	def compare_string(self, str1, str2):
		if len(str1) < len(str2):
			return False

		dic = [0 for _ in range(26)]

		for c in str1:
			dic[ord(c) - 65] += 1

		for c in str2:
			if dic[ord(c) - 65] == 0:
				return False
			else:
				dic[ord(c) - 65] -= 1
		return True

obj = Solution()
A = 'AABCD'
B = 'AABC'
print(obj.compare_string(A, B))