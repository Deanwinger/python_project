'''
输入两棵二叉树A，B，判断B是不是A的子结构
空树不是任意一个树的子结构
'''

#leetcode 572. Subtree of Another Tree, 类似题
#题18

class TreeNode(object):
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None

    def __bool__(self):
        return  False if self.val is None else True

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s or not t:
            return False
        result = False
        
        if s.val == t.val:
            result = self.is_included(s, t)
        if not result:
            result = self.isSubtree(s.left, t)
        if not result:
            result = self.isSubtree(s.right, t)
        return result

    def is_included(self, s, t):
        # 中止条件
        if t is None:
            return True

        if s is None:
            return False

        if s.val != t.val:
            return False

        return self.is_included(s.left, t.left) and self.is_included(s.right, t.right)

# leetcode 572, 此题与原题稍有区别, 要求必须是子树, 原题只检查是否是子结构
class SolutionOfEighteen:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s or not t:
            return False
        
        result = False
        
        if s.val == t.val:
            result = self.is_included(s, t)
        if not result:
            result = self.isSubtree(s.left, t)
        if not result:
            result = self.isSubtree(s.right, t)
        return result

    def is_included(self, s, t):
        # 中止条件
        if t is None and s is None:
            return True
        
        if t is None and s:
            return False
        
        if s is None and t:
            return False

        if s.val != t.val:
            return False

        return self.is_included(s.left, t.left) and self.is_included(s.right, t.right)

# 2019-6-21 独立写的, 很elegant, 对递归的理解又进了一步...
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        
        if not s or not t:
            return False
            
        if s.val == t.val:
            if self.s_include_t(s, t):
                return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def s_include_t(self, s, t):
        if not s and not t:
            return True
        
        if not s or not t:
            return False
        
        if s.val != t.val:
            return False
        
        return self.s_include_t(s.left, t.left) and self.s_include_t(s.right, t.right)

if __name__ == '__main__':
    pRoot1 = TreeNode(8)
    pRoot2 = TreeNode(8)
    pRoot3 = TreeNode(7)
    pRoot4 = TreeNode(9)
    pRoot5 = TreeNode(2)
    pRoot6 = TreeNode(4)
    pRoot7 = TreeNode(7)
    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot5.left = pRoot6
    pRoot5.right = pRoot7

    pRoot8 = TreeNode(8)
    pRoot9 = TreeNode(9)
    pRoot10 = TreeNode(2)
    pRoot8.left = pRoot9
    pRoot8.right = pRoot10

    S = Solution()
    print(S.find_subtree(pRoot1, pRoot8))