# leetcode 239. Sliding Window Maximum
# 程序员面试指南 第一章
# 本题的关键在于利用双端队列, collections.deque
from collections import deque

# 关键是保证最大的都在头部
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        maxq = my_deque()
        length = len(nums)
        for i in range(0, length): # i指代当前元素的index, j指代maxq队尾最后一个index
            while not maxq.is_empty() and nums[i]>=nums[maxq.peek_rear()]:
                maxq.pop_rear()
            
            maxq.append(i)

            e = maxq.peek_front()
            if e == i-k:
                maxq.pop_front()
            
            if i >= k-1:
                res.append(nums[maxq.peek_front()])
        return res

class my_deque:
    """double ended queue"""
    def __init__(self):
        self._queue = []
    
    def is_empty(self):
        """判断队列是否为空"""
        return not self._queue

    def append_left(self, item):
        """在队头添加元素"""
        self._queue.insert(0,item)

    def append(self, item):
        """在队尾添加元素"""
        self._queue.append(item)

    def pop_front(self):
        """从队头删除元素"""
        try:
            e = self._queue.pop(0)
        except IndexError:
            raise Exception("empty queue")
        else:
            return e

    def pop_rear(self):
        """从队尾删除元素"""
        try:
            e = self._queue.pop()
        except IndexError:
            raise Exception("empty queue")
        else:
            return e

    def peek_front(self):
        if not self.is_empty():
            return self._queue[0]
        return 

    def peek_rear(self):
        if not self.is_empty():
            return self._queue[-1]
        return 

    def size(self):
        """返回队列大小"""
        return len(self._queue)