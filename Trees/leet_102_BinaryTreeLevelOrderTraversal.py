# Problem:  Binary Tree Level Order Traversal
# Difficulty: Medium
# Category: Tree
# Leetcode 102: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Description:
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

	def level_order(self, root):
		if not root:
			return []
		ans = []
		queue = []
		queue.append(root)

		while queue:
			level = []
			for i in range(len(queue)):
				node = queue.pop(0)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
				level.append(node.val)
			ans.append(level)
		return ans
