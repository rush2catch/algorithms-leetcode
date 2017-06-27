
"""
use a list
"""
def reverse_str1(inputStr):

	reversedStr = []

	if len(inputStr) == 0:
		return None
	elif len(inputStr) == 1:
		reversedStr = inputStr
		return reversedStr
	else:
		for i in range(len(inputStr)):
			buff = inputStr.pop()
			reversedStr.append(buff)
		return reversedStr

# test case
test_str1 = []
test_str2 = ['a']
test_str3 = ['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(reverse_str1(test_str1))
print(reverse_str1(test_str2))
print(reverse_str1(test_str3))


"""
use a string
"""
def reverse_str2(inputStr):

	reversedStr = ''
	if len(inputStr) <= 1:
		return inputStr
	else:
		for i in range(len(inputStr)):
			reversedStr += inputStr[len(inputStr) - i -1]
		return reversedStr

# test case
testStr1 = ''
testStr2 = 'a'
testStr3 = 'gfedcba'
print(reverse_str2(testStr1))
print(reverse_str2(testStr2))
print(reverse_str2(testStr3))


"""
use string slicing
"""

def reverse_str3(inputStr):
	if len(inputStr) == 0:
		return None
	else:
		return inputStr[::-1]

# test case
str1 = ''
str2 = 'a'
str3 = 'gfedcba'
print(reverse_str3(str1))
print(reverse_str3(str2))
print(reverse_str3(str3))