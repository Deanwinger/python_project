# leetcode 538. Convert BST to Greater Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 2019-7-6 方法有效, 但是应该有更优的做法, to be finished
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        rec = []
        g = []
        self.get_inorder_rec(root, rec=rec, g=g)
        n = len(rec)
        for i in range(n):
            g[i].val = sum(rec[i:])
        return root 
        
        
    def get_inorder_rec(self, root, rec=[], g=[]):
        if not root:
            return
        
        self.get_inorder_rec(root.left, rec=rec, g=g)
        g.append(root)
        rec.append(root.val)
        self.get_inorder_rec(root.right, rec=rec, g=g)
        return
        