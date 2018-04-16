"""
 1.二叉树的遍历（深度， 广度遍历）
 2.堆排序
 3.AVL Tree
 3. Red Black Tree
"""
class QueueUnderflow(ValueError):
    pass

class SQueue(object):
    def __init__(self, init_len=8):
        self._len = init_len  # length of mem-block
        self._elems = [0]*init_len
        self._head = 0  # index of head element
        self._num = 0   # number of elements
        
    def is_empty(self):
        return self._num == 0
    
    def peek(self):
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]

    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head+1) % self._len
        self._num -= 1
        return e
    
    def enqueue(self, elem):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head+self._num) % self._len] = elem
        self._num += 1
        
    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0

class BinTNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# def levelorder(root, proc):
#     qu = SQueue()
#     qu.enqueue(root)

#     while not qu.is_empty():
#         n = qu.dequeue()
#         if root is None:
#             continue
#         qu.enqueue(root.left)
#         qu.enqueue(root.right)
#         proc(root.value)

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


if __name__ == "__main__":
    root = BinTNode(1, BinTNode(2, BinTNode(3), BinTNode(4)), BinTNode(5))
    levelorder(root, print)
