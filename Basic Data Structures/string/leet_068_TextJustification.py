# Problem:  Text Justification
#  Difficulty: Hard
# Category: String
# Leetcode 68: https://leetcode.com/problems/text-justification/description/
# Description:
"""
Given an array of words and a length L,
format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.
For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.
Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""


class Solution(object):

	def justification(self, words, max_length):
		count_word = 0
		count_char = 0
		count_line = 0
		line = [[]]
		i = 0
		while i < len(words):
			count_word += 1
			count_char += len(words[i])
			if count_char + count_word - 1 <= max_length:
				line[count_line].append(words[i])
			else:
				count_word = 1
				count_char = len(words[i])
				line.append([words[i]])
				count_line += 1
			i += 1
			"""
			if count_char <= max_length:
				line[count_line].append(words[i])
			else:
				if count_char - 1 <= max_length:
					line[count_line].append(words[i])
					count_line += 1
					line.append([])
					count_char = 0
				else:
					line.append([words[i]])
					count_line += 1
					count_char = len(words[i]) + 1
			"""

		print(line)

		for i in range(len(line)):
			count_char = 0
			spaces = 0
			count_words = 0
			if len(line[i]) == 1:
				line[i][0] += (max_length - len(line[i][0])) * ' '
			else:
				for j in range(len(line[i])):
					count_words = len(line[i])
					count_char += len(line[i][j])
				for k in range(len(line[i])):
					if k == len(line[i]) - 1:
						continue
					else:
						spaces = (max_length - count_char) // (count_words - 1)
						line[i][k] += spaces * ' '
				if spaces * (count_words - 1) < max_length - count_char:
					line[i][0] += (max_length - count_char - spaces*(count_words-1)) * ' '

		res = []
		for i in range(len(line)):
			temp = ''
			for word in line[i]:
				temp += ''.join(word)
			res.append(temp)

		return res



obj = Solution()
w1 = ["This", "is", "an", "example", "of", "text", "justification."]
#print(obj.justification(w1, 16))
print(obj.justification(w1, 18))


