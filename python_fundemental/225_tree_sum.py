# leetcode 437. 路径总和 III



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 2019-7-6 这个题目多做几次, 感受一下递归的魅力
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        count = self.get_path(root, sum)

        return self.pathSum(root.left, sum) + self.pathSum(root.right, sum) + count

    
    def get_path(self, root, target):
        if not root:
            return 0
        
        count = 0
        target -= root.val
        if target == 0:
            count += 1
            
        return self.get_path(root.left, target) + self.get_path(root.right, target) + count