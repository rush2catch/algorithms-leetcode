# Problem:   Binary Tree Post-order Traversal
# Difficulty: Hard
# Category: Tree
# Leetcode 145: https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Description:
"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
	def postorder(self, root):
		if root is None:
			return []
		curr = root
		res = []
		stack = []

		while curr or stack:
			if curr:
				stack.append(curr)
				res.insert(0, curr.val)
				curr = curr.right
			else:
				node = stack.pop()
				curr = node.left
		return res
