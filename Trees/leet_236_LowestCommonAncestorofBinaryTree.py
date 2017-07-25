# Problem:  Lowest Common Ancestor of a Binary Tree
# Difficulty: Medium
# Category: Tree
# Leetcode 236: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/#/description
# Description:
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes v and w as the lowest node in T
that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2_       0       8
         /   \
         7    4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""

from Tree import BinaryTree


class Solution(object):

	def lowestCommonAncestor(self, root, A, B):
		if root == None or root == A or root == B:
			return root

		left = self.lowestCommonAncestor(root.leftChild, A, B)
		right = self.lowestCommonAncestor(root.rightChild, A, B)

		if left is not None and right is not None:
			return root
		if left is not None and right is None:
			return left
		if right is not None and left is None:
			return right
		return None


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

# to verify the tree is constructed correctly
"""
Node_3.inorder()
print()
Node_3.preorder()
print()
Node_3.postorder()
"""


obj = Solution()
print(obj.lowestCommonAncestor(Node_5, Node_6, Node_7).key)
# print(obj.lowestCommonAncestor(Node_5, Node_3, Node_1).key)
print(obj.lowestCommonAncestor(Node_1, Node_0, Node_8).key)
print(obj.lowestCommonAncestor(Node_3, Node_4, Node_0).key)
