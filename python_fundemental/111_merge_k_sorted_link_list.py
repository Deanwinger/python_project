# leetcode 23. 合并K个排序链表

'''
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

思路: 可以最小堆解决， 把所有的链表元素读入一个最小堆里，然后每次从堆取出一个最小元素构造
成一个新链表，提交通过。堆可以用 python heapq 模块快速实现
'''

from heapq import heappop, heapify


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:        
        h = []
        for node in lists:
            while node:
                h.append(node.val)
                node = node.next
        
        if not h:
            return
        heapify(h)
        dum = head = ListNode(heappop(h))
        while h:
            node = ListNode(heappop(h))
            head.next = node
            head = head.next
            
        # head.next = None
        return dum