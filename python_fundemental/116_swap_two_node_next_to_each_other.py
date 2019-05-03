# leetcode 24. 两两交换链表中的节点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 2019-5-3 非常明显的递归, one take, 一次性pass
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        # 奇数节点链表
        if head and head.next is None:
            return head
        # 偶数节点链表
        if head and head.next and head.next.next is None:
            pre = head.next
            head.next = None
            pre.next = head
            return pre
        
        fast = head.next.next
        pre = head.next
        head.next = self.swapPairs(fast)
        pre.next = head
        return pre