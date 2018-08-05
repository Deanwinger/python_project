# leetcode 92. 反转链表 II

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        cornor case: 
            1. m对应第一个时, 需要返回不同的head节点
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == 1:
            dummy = head
            p = head.next
            while n > 1:
                temp = p.next
                p.next = head
                head = p
                p = temp
                n -= 1
            dummy.next = p
            return head
        else:
            k = n-m
            if k == 0:
                return head
            dummy = head
            while m > 1:
                pre = head
                head = head.next
                m -= 1
            tail = head
            p = head.next
            while k >0:
                temp = p.next
                p.next = head
                head = p
                p = temp
                k -= 1
            pre.next = head
            tail.next = p
            return  dummy