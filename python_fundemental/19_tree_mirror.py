'''
操作给定的二叉树，将其变换为源二叉树的镜像。
'''

#leetcode 226
#题19, 简单的先序遍历

class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, head):
        """
        非常经典的递归
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        
        if root.left is None and root.right is None:
            return root
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__=='__main__':
    pass

