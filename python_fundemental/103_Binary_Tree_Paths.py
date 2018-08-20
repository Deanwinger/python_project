# leetcode 257. Binary Tree Paths

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        rec = []
        g = []
        self.find_path(root, rec, g)
        return g
        
    def find_path(self, root, rec, g):
        rec.append(root)
        
        isleaf = root.left is None and root.right is None
        if isleaf:
            tem = [str(r.val) + "->" for r in rec]
            t = ''.join(tem)
            g.append(t[:-2])
        
        if root.left:
            self.find_path(root.left, rec, g)
        if root.right:
            self.find_path(root.right, rec, g)
        
        rec.pop()