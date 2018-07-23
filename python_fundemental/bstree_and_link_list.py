'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

# leetcode 题426， 可惜不能在线测
# LintCode 题378
# 题27

class Solution:
    """
    @param: root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        if root is None:
            return
        