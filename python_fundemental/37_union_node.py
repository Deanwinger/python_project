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


        