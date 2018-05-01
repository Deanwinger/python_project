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
    def __init__(self):
        pass