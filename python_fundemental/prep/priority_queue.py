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

    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last-1)//2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e

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
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)

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

if __name__ == '__main__':
    alist = [1,6,2,7,4,3,5]
    # heap_sort(alist)
    # print(alist) #[7, 6, 5, 4, 3, 2, 1]
    p = PrioQueue(alist)
    p.buildheap()
    print(p._elems)