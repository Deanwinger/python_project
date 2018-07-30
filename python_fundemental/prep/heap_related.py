# heap Python实现

# 今天就把堆这个数据结构玩残
"""
通常使用binary heap
    1. heap的结构性质:
        (1). 堆是一棵被完全填满的二叉树， 有可能的例外是在最底层， 底层上的元素从左到右填入，这样的树也被称为完全二叉树；
        (2). 完全二叉树到线性结构有自然的双向映射, 如果n个结点的完全二叉树的结点按层级并依次从左至右的顺序从0开始编号， 对任一结点i(0 <= i <= n-1)；
            a. 序号为0的节点是根；
            b. 对于i>0, 其父结点的编号是 (i-1)/2;
            c. 若 2×i+1 < n, 其左子结点序号2×i+1， 否则它无左子结点；
            d. 若 2×i+2 < n, 其右子结点序号2×i+2， 否则它无右子结点；
            e. 完全二叉树， 从下标end//2的位置开始（包括该位置），后面表元素都是二叉树的叶子节点；
    2. 堆序性:
        (1). 除根结点外， 任一结点里所保存的数据，先于或等于其子结点里的数据；
        (2). 位于树中不同路径上的元素， 不关心其顺序关系；
            a. 插入时， 先在列表的最后插入一个空穴， 然后percolate up(上滤)（空穴上行）
            b. 删除时， percolate down（空穴下行）， 可能导致为保持堆序性，
"""

class PrioQueueError(ValueError):
    pass

# 基于（小顶）堆的优先序列
class PrioQueue:
    """ Implementing priority queues using heaps
    """
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]
    
    def enqueue(self, e):
        self._elems.append(None)  # add a dummy element
        self.siftup(e, len(self._elems)-1)

    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last-1)//2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin*2+1
        while j < end:    # invariant: j == 2*i+1
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1    # elems[j] <= its brother
            if e < elems[j]:     # e is the smallest of the three
                break
            elems[i] = elems[j]  # elems[j] is the smallest, move it up
            i, j = j, 2*j+1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)

# 堆排序
def heap_sort(elems):
    def siftdown(elems, e, begin, end):
        i, j = begin, begin*2+1
        while j < end:  # invariant: j == 2*i+1
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1  # elems[j] <= its brother
            if e < elems[j]:     # e is the smallest of the three
                break
            elems[i] = elems[j]  # elems[j] is the smallest, move it up
            i, j = j, 2*j+1
        elems[i] = e
        
    end = len(elems)
    for i in range(end//2, -1, -1):
        siftdown(elems, elems[i], i, end)
    for i in range((end-1), 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)