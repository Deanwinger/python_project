# leetcode 102




class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        rec = []
        que = []
        que.append((root, 0))
        while que:
            node_info = que.pop(0)
            node = node_info[0]
            level = node_info[1]+1
            rec.append((node.val, node_info[1]))
            if node.left:
                que.append((node.left, level))
            if node.right:
                que.append((node.right, level))
                
        ret = self.get_level_info(rec)
        return ret
        
    # 尝试用map reduce写下
    def get_level_info(self, rec):
        if not rec:
            return [[]]
        
        if len(rec) == 1:
            return [[rec[0][0]]]

        n = len(rec)
        ret = []
        i = 0
        pre = 0
        temp = []
        while i < n:
            node_val = rec[i][0]
            level = rec[i][1]
            if level == pre:
                temp.append(node_val)
            else:
                ret.append(temp[::])
                temp = []
                temp.append(node_val)
            pre = level
            i += 1
            if i == n:
                ret.append(temp[::])
        return ret