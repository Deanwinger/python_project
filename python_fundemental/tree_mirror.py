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

class Solution(object):
    def invertTree(self, head):
        """非常经典的递归"""
        if head is None:
            return
        if head.left is None and head.right is None:
            return head
        head.left, head.right = self.invertTree(head.left), self.invertTree(head.right)
        return head


if __name__=='__main__':
    pass

