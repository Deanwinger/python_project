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
    def find_subtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        result = False
        if s.val == t.val:
            #此判断用于寻找与子树相同的root节点, 然后判断是否有相同的结构
            result = self.s_includes_t(s, t)
        if not result:
            result = self.find_subtree(s.left, t)
        if not result:
            result = self.find_subtree(s.right, t)
        return result

    def s_includes_t(self, s, t):
        if not t:
            return True
        if not s:
            return False
        if s.val != t.val:
            return False
        return self.s_includes_t(s.left, t.left,) and \
                self.s_includes_t(s.right, t.right)




if __name__ == '__main__':
    node1 = TreeNode(1)