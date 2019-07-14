'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
'''

from random import randint

import heapq

# 题30， 最小的K个数

# leetcode 215. 数组中的第K个最大元素

# 类似题 leetcode 230. Kth Smallest Element in a BST -- 此题用中序遍历就好

class Solution:
    def kthSmallest(self, root, k):
        """
        解法1： 正常的排序, 快排, 堆排, 归并都行
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        n = len(nums)
        index = self.partition(nums, start, end)
        while index != n-k:
            if index > n-k:
                end = index-1
                index = self.partition(nums, start, end)
            else:
                start = index+1
                index = self.partition(nums, start, end)
        return nums[index]
    
    def partition(self, nums, lo, hi):
        if lo>= hi:
            return hi
        pivot = lo
        i = lo+1
        j = hi
        while True:
            while nums[i] < nums[pivot]:
                if i == hi:
                    break
                i += 1
                    
            while nums[j] > nums[pivot]:
                if j == lo:
                    break
                j -=1
                    
            if i >= j:
                break
                    
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        nums[lo], nums[j] = nums[j], nums[lo]
        return j

    def k_smallest(self, nums, k):
        """
        解法2，使用 堆, 用堆就好了, 为什么要用优先队列
        :type: nums: [list]
        :rtype: [list]
        """
        # 当 K大于输入长度, 则返回[]
        if len(nums) < k:
            return []
        array = BPrioQueue(nums)
        n = len(array) - k
        while n:
            array.dequeue()
            n -= 1
        rec = []
        while len(array):
            rec.append(array.dequeue())
        return rec
        


# 果然自己写的pq没有heapq快
# 自己构造基于（大顶）堆的优先队列
# 也可使用Python自带模块heapq
class BPrioQueue:
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
        while i > 0 and e > elems[j]:
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
            if j+1 < end and elems[j+1] > elems[j]:
                j += 1    # elems[j] <= its brother
            if e > elems[j]:     # e is the smallest of the three
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

    def __repr__(self):
        return "PrioQueue<{}>".format(self._elems)


# 类似题 leetcode 230. Kth Smallest Element in a BST -- 此题用中序遍历就好
from queue import Queue

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        解法1: 树的中序
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        q = Queue(0)
        self.inorder(root, q)
        while k>1:
            q.get()
            k -= 1
        return q.get()
        
    # 遍历用递归完成, 效率很低
    def inorder(self, root, q):
        if root is None:
            return
        self.inorder(root.left, q)
        q.put(root.val)
        self.inorder(root.right, q)
        return

    def kthSmallest_v2(self, root, k):
        """
        解法2: 树的中序, 非递归
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        rec = self.inorder_nonrec(root)
        return rec[k-1]
    
    def inorder_nonrec(self, t):
        rec = []
        s = SStack()
        while t or not s.is_empty():
            while t:
                s.push(t)
                t = t.left
            t = s.pop()
            rec.append(t.val)
            t = t.right
        return rec
              
        
# 基于顺序表的实现
class SStack:
    def __init__(self):
        self._elems = []
    
    def is_empty(self):
        return not self._elems

    def top(self):
        if not self._elems:
            raise StackUnderflow("empty SStack")
        return self._elems[-1]
    
    def push(self, elem):
        self._elems.append(elem)

    # 弹出最后一个元素
    def pop(self):
        if not self._elems:
            raise StackUnderflow("empty SStack")
        return self._elems.pop()
        


# 2019-6-19
class Solution3:
    def GetLeastNumbers_Solution(self, nums, k):
        # write code here
        n = len(nums)
        if not n:
            return
        if n == 1:
            return nums[0]
        
        start = 0
        end = n-1
        target = k-1
        ind = self.partition(nums, start, end)
        while ind != target:
            if ind < target:
                start = ind + 1
            else:
                end = ind - 1
            ind = self.partition(nums, start, end)
        return nums[:k]
    
    def partition(self, nums, lo, hi):
        # 非常关键, corner case [2, 3], 没有该条件就直接报错, 其实这里改为== 更合理, 注意, partition之前, 肯定是保证有两个元素以上, 当不停的partition时, 范围不断缩小, 当只剩下两个时, 非此即彼
        if lo == hi:
            return hi
        i = lo+1
        j = hi

        pivot = lo
        while True:
            while nums[i] < nums[pivot]:
                if i == hi:
                    break
                i += 1

            while nums[j] > nums[pivot]:
                if j == lo:
                    break
                j -= 1

            if i>=j:
                break
            else:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[lo], nums[j] = nums[j], nums[lo]
        return j













if __name__ == "__main__":
    a = [4,5,1,6,2,7,3,8]
    s = Solution3()
    print(s.GetLeastNumbers_Solution(a, 4))



