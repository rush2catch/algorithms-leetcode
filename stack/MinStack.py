#! /usr/bin/env python3
class MinStack(object):

    def __init__(self):
        """
        initialize the data structure
        :return:
        """
        self.s = []

    def push(self,x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.s.append((x,curMin))

    def pop(self):
        if len(self.s) == 0:
            return None
        self.s.pop()


    def top(self):
        if len(self.s) == 0:
            return None
        else:
            return self.s[len(self.s)-1][0]


    def getMin(self):
        if len(self.s) == 0:
            return None
        else:
            return self.s[len(self.s)-1][1]
