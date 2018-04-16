"""
 1.二叉树的遍历（深度， 广度遍历）
 2.堆排序
 3.AVL Tree
 4.Red Black Tree
"""


rec = []
#树节点
class BinTNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#树的深度遍历
# def high_rank(root):
#     rec = []
#     def pre_order(root):
#         if not root:
#             return
#         # print(root.value)
#         rec.append(root.value)
#         pre_order(root.left)
#         pre_order(root.right)
#         return 
#     pre_order(root)
#     print(rec)

#树的先序遍历 --递归实现
def pre_order(root, rec):
    if not root:
        return
    # print(root.value)
    rec.append(root.value)
    pre_order(root.left, rec)
    pre_order(root.right, rec)
    return rec

#树的中序遍历 --递归实现
def inorder(t, proc):
    if t is None:
        return
    inorder(t.left, proc)
    proc(t.value)
    inorder(t.right, proc)

#树的后序遍历 --递归实现
def postorder(t, proc):
    if t is None:
        return
    postorder(t.left, proc)
    postorder(t.right, proc)
    proc(t.value)

#二叉树的先序遍历 --非递归实现
def pre_order_nonrec(root, proc):
    s = SStack()
    while root is not None or not s.is_empty():
        while root is not None:
            proc(root.value)
            s.push(root.right)
            root = root.left
        root = s.pop()

#二叉树的中序遍历 --非递归实现
def in_order_nonrec(root, proc):
    s = SStack()
    while t or not s.is_empty():
        while t:
            s.push(t)
            t = t.left
        t = s.pop()
        proc(t.value)
        t = t.right

#二叉树的后序遍历 --非递归实现
def post_order_nonrec(root, proc):
    s = SStack()
    while t or not s.is_empty():
        while t:
            s.push(t)
            t = t.left if t.left else t.right
        t = s.pop()
        proc(t.value)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            t = None
    
#树的广度(层次)遍历
def levelorder(t, proc):
    q = SQueue()
    q.enqueue(t)
    while not q.is_empty():
        t = q.dequeue()
        if t is None:
            continue
        q.enqueue(t.left)
        q.enqueue(t.right)
        proc(t.value, end=" ")

if __name__== "__main__":
    t1 = BinTNode(1, BinTNode(2, BinTNode(3), BinTNode(4)), BinTNode(5))
    # pre_order(t1)
    # print(rec)
    # high_rank(t1)
    pre_order(t1, rec)
    print(rec)