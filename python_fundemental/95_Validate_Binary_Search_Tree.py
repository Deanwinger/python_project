# leetcode 98. Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
            
        stack = []
        h = root
        while h.left:
            h = h.left
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root is h:
                pass
            else:
                if h.val >= root.val:
                    return False
                h = root
            root = root.right
        return True
                