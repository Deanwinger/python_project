# leetcode 236. Lowest Common Ancestor of a Binary Tree
# leetcode 235 简易版, 二叉搜索树
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

    # 9.4突然发现, 这个函数才是真正面向对象的递归写法, 要好好研究    
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

    def find_path(self, root, node, rec, g):
        if not root:
            return
        rec.append(node)

        node_found = root is node
        if node_found:
            g = list(rec)
            return
        if root.left:
            self.find_path(root.left, node, rec, g)
        
        if root.right:
            self.find_path(root.right, node, rec, g)
        return 



class Solution:
    def lowestCommonAncestor(self, root, p, q):
        rec = []
        g = []
        self.find_path(root, p, rec, g)
        self.find_path(root, q, rec, g)
        g1, g2 = g[0], g[1]
        same_elems = [r for r in g1 and r in g2]
        return same_elems[-1]

    def find_path(self, root, node, rec, g):
        if not root:
            return
        
        rec.append(root.val)
        if root is node:
            g.append(list(rec))

        if root.left:
            self.find_path(root.left)

        if root.right:
            self.find_path(root.right)
        rec.pop()
        return

