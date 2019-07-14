'''
输入两个链表，找出它们的第一个公共结点。
'''

#题37 非常容易, 不需深究
#leetcode 160 Intersection of Two Linked Lists 


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        思路，先遍历， 判断哪家长， 长的先走几步
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        
        dummyA = headA
        dummyB = headB
        m = 1
        while headA:
            headA = headA.next
            m += 1
        
        n = 1
        while headB:
            headB = headB.next
            n += 1
        
        s = abs(m-n)
        if m > n:
            while s:
                dummyA = dummyA.next
                s -= 1
        if m < n:
            while s:
                dummyB = dummyB.next
                s -= 1
        
        while dummyA and dummyB:
            if dummyA == dummyB:
                return dummyA
            dummyA = dummyA.next
            dummyB = dummyB.next
        return None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 2019-6-8 一个非常elegant 的解法, 虽然如此, 但是需要考虑的细节增加了
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        定义两个指针, 第一轮让两个到达末尾的节点指向另一个链表的头部, 最后如果相遇则为交点(在第一轮移动中恰好抹除了长度差)
        两个指针等于移动了相同的距离, 有交点就返回, 无交点就是各走了两条指针的长度
        """
        if headA is None or headB is None:
            return
        
        pA = headA
        pB = headB
        while pA and pB:
            if pA is pB:
                return pA
            
            pA = pA.next            
            pB = pB.next
            if pA is None and pB is None:
                return 
            if pA is None:
                pA = headB
            if pB is None:
                pB = headA
        return
        