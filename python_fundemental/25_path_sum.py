'''
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''

#leetcode 113. Path Sum II, 类似还有112. Path Sum 和 437. Path Sum III
#题25

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 这个题目值得反复回味
class Solution:
    """二叉树的先序遍历相关"""
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        sum -= root.val
        stack = []

        if sum == 0 and root.left is None and root.right is None:
            return [[root.val]]
        
        leftStack = self.pathSum(root.left, sum)
        for i in leftStack:
            i.insert(0, root.val)
            stack.append(i)
            
        rightStack = self.pathSum(root.right, sum)
        for i in rightStack:
            i.insert(0, root.val)
            stack.append(i)
        return stack

#8.20 by self, 很简单的先序
class Solution:
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        g = []
        rec = []
        cur = 0
        self.find_path(root, target, rec, cur, g)
        return g
    
    def find_path(self, root, target, rec, cur, g):
        cur += root.val
        rec.append(root.val)
        
        isleaf = root.left is None and root.right is None
        if cur == target and isleaf:
            g.append(list(rec))
        if root.left:
            self.find_path(root.left, target, rec, cur, g)
        if root.right:
            self.find_path(root.right, target, rec, cur, g)
        
        cur -= root.val
        rec.pop()

if __name__=='__main__':
    pass