# leetcode 703. Kth Largest Element in a Stream


# 据说堆序对于最大Kth element 相关题目很好使, 但是随便写写就小100行了
# 8.27 重写, 用到大顶堆, 完全错误, 试想, 如果最大的三个元素, 分别是10, 8, 7, 
# 第四大的数字是6, 如果这个时候add一个9, 用大顶堆的话, 堆顶元素就是9 ,但是实际上应该是7, 
# 所以只能用小顶堆 

class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        length = len(nums)
        self.heap = PrioQueue(nums)
        self.kth_num = self.get_kth_num(length-k) if length-k>0 else None
        self.limit = k
        
    def get_kth_num(self, m):
        while m:
            self.heap.dequeue()
            m -= 1
        return self.heap.peek()

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.heap.enqueue(val)
        
        if len(self.heap) < self.limit:
            return
        if len(self.heap) > self.limit:
            self.heap.dequeue()

        self.kth_num = self.heap.peek()
        return self.kth_num

# 基于（小顶）堆的优先队列
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
            # raise PrioQueueError("in peek")
            return
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
            # raise PrioQueueError("in dequeue")
            return None
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
        
    def __len__(self):
        return len(self._elems)
    

# 2019-7-1, 这题需要注意的是, 当堆的元素少于k时, 直接返回堆顶元素

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._heap = self.get_heap(nums, k)

    def add(self, val: int) -> int:
        n = len(self._heap)
        k = self._k
        if n < k:
            heapq.heappush(self._heap, val)
        else:
            top = self._heap[0]
            if val > top:
                heapq.heappush(self._heap, val)
                heapq.heappop(self._heap)
        return self._heap[0]
    
    def get_heap(self, nums, k):
        n = len(nums)
        h = list(nums)
        t = h[:k]
        heapq.heapify(t)
        for i in range(k, n):
            top = t[0]
            if h[i] > top:
                heapq.heappush(t, h[i])
                heapq.heappop(t)
        return t
