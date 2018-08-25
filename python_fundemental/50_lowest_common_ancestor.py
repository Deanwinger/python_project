# leetcode 236. Lowest Common Ancestor of a Binary Tree

# 题50
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        rec1 = []
        rec2 = []
        self.get_path(root, p, rec1)
        self.get_path(root, q, rec2)
        return [r for r in rec1 if r in rec2][-1]
    

    # 此函数非常的关键, 反复研究, 获取路径的函数
    def get_path(self, root ,p, rec):
        rec.append(root)
        if root is p:
            return True
        
        found = False
        if not found and root.left:
            found = self.get_path(root.left, p, rec)
        
        if found:
            return found

        if not found and root.right:
            found = self.get_path(root.right, p, rec)
        
        if not found:
            rec.pop()
        return found

# 8.25 重做, 发现基本上就是25题的思路即可, 对于这种找存在的递归, 值得好好反复思考;
class Solut(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        rec1 = []
        rec2 = []
        self.find_path(root, p, rec1)        
        self.find_path(root, q, rec2)
        return [r for r in rec1 if r in rec2][-1]
        
    def find_path(self, root, node, rec):
        if not root:
            return False
        
        rec.append(root)
        found = False
                
        if root is node:
            return True
        
        found = self.find_path(root.left, node, rec)
        if not found:
            found = self.find_path(root.right, node, rec)
            
        if not found:
            rec.pop()
            
        return found