'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
# leetcode 105 -- 剑指offer 题 6
# leetcode 106. 从中序与后序遍历序列构造二叉树
# leetcode 889. 根据前序和后序遍历构造二叉树
# 关键在于递归遍历， 关键点就在于找到根节点， 然后对于每个子树，都用找根节点确定左右子树的方式递归的进行下去
# 2019.2.13 
# 2019.4.9 


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre and not tin:
            return None

        if set(pre) != set(tin):
            return None

        root = Node(pre[0])
        i = tin.index(pre[0])
        root.left = reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.right = reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root
        
#2018.8.9 re_do, 千万注意index, [1: i+1], [:i], 两者才包含同样多的数
class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre and not tin:
            return
        
        root = TreeNode(pre[0])
        i = tin.index(pre[0])
        
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root



    
if __name__ == '__main__':
    pre = [1, 2, 3, 5, 6, 4]
    tin = [5, 3, 6, 2, 4, 1]
    print(reConstructBinaryTree(pre, tin))

