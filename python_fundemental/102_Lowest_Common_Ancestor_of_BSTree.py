# leetcode 235. Lowest Common Ancestor of a Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        bigger = q.val if q.val > p.val else p.val
        smller = p.val if p.val < q.val else q.val
        print("bigger is:")
        while  smller > root.val or root.val > bigger:
            if smller > root.val:
                root = root.right
            if root.val > bigger:
                root = root.left
        return root
        