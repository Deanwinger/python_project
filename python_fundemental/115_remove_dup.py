# leetcode 83. 删除排序链表中的重复元素


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        
        dum = head
        fast = head.next
        while fast:
            if head.val == fast.val:
                head.next = fast.next
                fast = fast.next
                continue
            head = head.next
            fast = fast.next
        return dum