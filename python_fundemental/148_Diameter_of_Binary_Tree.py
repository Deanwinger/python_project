# leetcode 543. Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 这一题有点tricky的就是, 有三种情况, 最长直径在左树, 或者是右树, 还可能是跨越左右树
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.get_length(root.left)
        right = self.get_length(root.right)
        
        o = left+right
        t = self.diameterOfBinaryTree(root.left)
        s = self.diameterOfBinaryTree(root.right)

        return max((t,s,o))
    
    def get_length(self, root):
        if not root:
            return 0
        return max(self.get_length(root.left), self.get_length(root.right))+1