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
# 此题可以用后序遍历的方法解决,  to be finished, 这种只需要出现一个异常就返回的递归要好好体会;
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

# 8.23 重写题39
class Solu(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1+max(left, right)