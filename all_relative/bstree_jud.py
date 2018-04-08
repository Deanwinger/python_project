"""
题目： 给予一个二叉树的根节点，验证该树是否是二叉搜索树，（在O(n)时间内

                 node1
              /        \
         node2          node3
        /     \        /     \
    node4    node5  node6     node7
"""

import unittest

class TreeNode(object):
    def __init__(self, val, leftNode=None, rightNode=None):
        self.val = val
        self.leftNode = leftNode
        self.rightNode = rightNode
    
    def __repr__(self):
        return "TreeNode(%s)" % self.val

root1 = None

root2 = TreeNode(1)


class MyTests(unittest.TestCase):
    def test_bstree_judge(self, root):
        pass