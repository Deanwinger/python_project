# 题39 二叉树的深度  leetcode 104. Maximum Depth of Binary Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left + 1, right + 1)

    def max_depth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# 拓展 leetcode 110. Balanced Binary Tree
'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if abs(left-right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left + 1, right + 1)


    def is_balanced(self, root):
        """解法2： 使用后序遍历来实现"""
        pass