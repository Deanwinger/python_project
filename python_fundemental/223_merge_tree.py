# leetcode 617 合并二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return
        
        if t1 and t2:
            t1.val = t1.val + t2.val
        elif t1 and not t2:
            return t1
        elif not t1 and t2:
            return t2
        else:
            return
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


# leetcode 111. 二叉树的最小深度
# 2019-6-26 迭代法 to be finished...

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        if root.left and root.right:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return min(left, right)+1
        if root.left:
            return self.minDepth(root.left)+1
        if root.right:
            return self.minDepth(root.right)+1