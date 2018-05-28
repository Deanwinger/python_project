from stack_related import SStack

"""
     字典的基本关联类 
"""

#树节点
class BinTNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    # 小于
    def __lt__(self. other):
        return self.key < other.key

    # 不大于
    def __le__(self, other):
        return self.key < other.key or self.key == other.key

    def __str__(self):
        return "Assoc({0},{1})".format(self.key, self.value)


"""
    2.二叉搜索树
    (1). 使二叉树成为二叉查找树的性质是：对于树中的每个节点X， 
        他的左子树中所有关键字（节点）值小于X的关键字（节点）值， 
        而他的右子树中所有关键字（节点）值大于X的关键字（节点）值；
    (2). 一颗节点中存储着关键码的二叉树是二叉搜索树，
        当且仅当通过'中序遍历'这颗二叉树得到的关键码序列是一个递增序列；
"""


# 根据二叉搜索树 定义一个字典类
 class DictBinTree:
    def __init__(self):
         self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        bt = self._root
        while bt:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None

    def insert(self, key, value):
        bt = self._root
        if bt is None:
            self._root = BinTNode(Assoc(key, value))
            return 
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left is None:
                    bt.left = BinTNode(Assoc(key, value))
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTNode(Assoc(key, value))
                    return 
                bt = bt.right
            else:
                bt.data.value = value
                return
    
    def values(self):
        """中序遍历, 返回值"""
        t, s = self._root, SStack()
        while t or not s.is_empty():
            while t:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.value
            t = t.right

    def entries(self):
        """中序遍历, 返回key, value"""
        t, s = self._root, SStack()
        while t or not s.is_empty():
            while t:
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.key, t.data.value
            t = t.right

    def delete(self, key):
        p, q = None, self._root # keep p the parent of q
        while q and q.data.key != key:
            p = q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right
        if q is None:
            return # key is not in the tree
        if q.left is None: # q没有左子树
            if p is None:
                self._root = q.right # q == self._root
            elif q is p.left:
                p.left = q.left
            else: 
                p.right = q.right #在q左子树为空的情况下，直接顶上去就好了
            return
        r = q.left # q有左子树
        while r.right:
            r = r.right
        r.right = q.right
        if p is None:
            self._root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left



    def print(self):
        for k, v in self.entries():
            print(k, v)
