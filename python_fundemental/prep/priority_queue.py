# 优先队列
# 优先队列的特点是： 存入其中的每项数据都有一个额外的值， 表示这个项的优先程度，称为其优先级

class PriorityQueueError(ValueError):
    pass


class PrioQue(object):
    """基于list的实现， 值越小具有越高的优先级"""
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def is_empty(self):
        return not self._elems    

    def peek(self):
        if self.is_empty():
            raise PriorityQueueError("on top")
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in pop")
        return self._elems.pop()

    def enqueue(self, e):
        i = len(self._elems)-1
        while i >= 0:
            if self._elems[i] <= e:
                # 此处的等于条件保证了优先级相同的元素可以先进先出
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)


class PrioQueue(object):
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()
    
    def is_empty(self):
        return not self._elems
    
    def peek(self):
        if self.is_empty():
            raise PriorityQueueError("in peek")
        return self._elems[0]

    def enqueue(self, e):
        pass

    def dequeue(self):
        pass

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end, -1, -1):
            self.siftdown(self._elems[i], i, end)