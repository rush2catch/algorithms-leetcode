# Problem:  Minimum Depth of Binary Tree
# Difficulty: Easy
# Category: Tree
# Leetcode 111: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/#/description
# Description:
"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2_       0       8
         /   \
         7    4
"""


from Tree import BinaryTree
import sys


class Solution(object):
	def mini_depth(self, root):
		if root is None:
			return 0
		return self.get_min(root)

	def get_min(self, root):
		if root is None:
			return sys.maxsize
		if root.leftChild is None and root.rightChild is None:
			return 1
		return min(self.get_min(root.leftChild), self.get_min(root.rightChild)) + 1

# Construct a binary tree to test
Node_3 = BinaryTree(3)
Node_3.insertLeft(5)
Node_3.insertRight(1)
Node_5 = Node_3.getLeftChild()
Node_1 = Node_3.getRightChild()

Node_5.insertLeft(6)
Node_6 = Node_5.getLeftChild()
Node_5.insertRight(2)
Node_2 = Node_5.getRightChild()

Node_2.insertLeft(7)
Node_7 = Node_2.getLeftChild()
Node_2.insertRight(4)
Node_4 = Node_2.getRightChild()

Node_1.insertLeft(0)
Node_0 = Node_1.getLeftChild()
Node_1.insertRight(8)
Node_8 = Node_1.getRightChild()

obj = Solution()
print(obj.mini_depth(Node_3))
print(obj.mini_depth(Node_5))
print(obj.mini_depth(Node_6))
print(obj.mini_depth(Node_6.getLeftChild()))
