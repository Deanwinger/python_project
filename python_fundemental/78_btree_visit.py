# leetcode 144. 二叉树的前序遍历
# leetcode 94. 二叉树的中序遍历
# leetcode 145. 二叉树的后序遍历
# leetcode 102. 二叉树的层次遍历

from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 二叉树的前序遍历
class SolutionOfPreOrder:
    def preorderTraversal(self, root):
        """
        一 先序遍历的递归实现
        :type root: TreeNode
        :rtype: List[int]
        """
        rec = []
        self.pre_order(root, rec)
        return rec
    
    def pre_order(self, root, rec):
        if not root:
            return
        rec.append(root.val)
        self.pre_order(root.left, rec)
        self.pre_order(root.right, rec)
        return

    def preorderTraversal_nonrec(self, root):
        """
        二 先序遍历的非递归实现
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        rec = []
        while root or stack:
            while root:
                rec.append(root.val)
                stack.append(root.right)
                root = root.left
            root = stack.pop()
        return rec
        

# 二叉树的中序遍历
class SolutionOfInOrder:
    def inorderTraversal(self, root):
        """
        一 中序遍历的递归实现
        :type root: TreeNode
        :rtype: List[int]
        """
        rec = []
        self.in_order(root, rec)
        return rec

    def in_order(self, root, rec):
        if not root:
            return

        self.in_order(root.left, rec)
        rec.append(root.val)
        self.in_order(root.right, rec)
        return 


    def inorderTraversal_nonrec(self, root):
        """
        二 中序遍历的非递归实现
        :type root: TreeNode
        :rtype: List[int]
        """
        rec = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            rec.append(root.val)
            root = root.right
        return rec

# 二叉树的后序遍历
class SolutionOfPostOrder:
    def inorderTraversal(self, root):
        """
        一 后序遍历的递归实现
        :type root: TreeNode
        :rtype: List[int]
        """
        rec = []
        self.post_order(root, rec)
        return rec

    def post_order(self, root, rec):
        if not root:
            return

        self.in_order(root.left, rec)
        self.in_order(root.right, rec)
        rec.append(root.val)
        return 

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rec = []        
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left if root.left else root.right
            root = stack.pop()
            rec.append(root.val)
            if stack and stack[-1].left is root:
                root = stack[-1].right
            else:
                root = None
        return rec
            
# 层次遍历
# 层次遍历
class SolutionOfLevelTravel:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rec = []
        que = Queue()
        que.put(root)
        while not que.empty():
            root = que.get()
            if root is None:
                continue
            rec.append(root.val)
            que.put(root.left)
            que.put(root.right)
        return rec

