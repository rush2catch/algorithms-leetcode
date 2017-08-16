# Problem:   Binary Tree Inorder Traversal
# Difficulty: Medium
# Category: Tree
# Leetcode 94: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Description:
"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
	def inorder(self, root):
		if root is None:
			return []
		curr = root
		stack = []
		res = []

		while curr or stack:
			if curr:
				stack.append(curr)
				curr = curr.left
			else:
				node = stack.pop()
				res.append(node.val)
				curr = curr.right
		return res