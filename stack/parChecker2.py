from stack import Stack

#class Solution(object):

def parChecker2(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if top != symbol:
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

#obj = Solution()
print(parChecker2('[][[[{](){}][}[['))
print(parChecker2('()'))