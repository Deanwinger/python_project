# leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder == postorder == []:
            return None
        
        n = len(inorder)
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        # for i in range(n):
        #     if inorder[i] == root:
        #         break
        
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        
        return root

if __name__ == "__main__":
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    s = Solution()
    s.buildTree(inorder, postorder)