# leetcode 98. 验证二叉搜索树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 2019-7-7 肯定有更好的方法, to be finished...
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 方法一                
        rec = []
        ret = True
        self.post_order(root, rec=rec)
        res = sorted(rec)
        if res != rec:
            ret = False
        res = list(set(res))
        if len(res) != len(rec):
            ret = False
        return ret
    
    def post_order(self, root, rec=[]):
        if not root:
            return
        
        self.post_order(root.left, rec=rec)
        rec.append(root.val)
        self.post_order(root.right, rec=rec)
        return