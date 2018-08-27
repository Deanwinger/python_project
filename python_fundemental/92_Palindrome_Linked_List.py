# leetcode 234. Palindrome Linked List


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        
        # 此处是找中点, 很重要
        head1 = head2 = head
        while head2.next and head2.next.next:
            head1 = head1.next 
            head2 = head2.next.next

        p = head1.next # 反转之后第一个节点
        head1.next = None # head1 表示中点, 中点之后的反转
        while p:
            temp = p.next
            p.next = head1
            head1 = p
            p = temp
        while head1 and head:
            if head1.val != head.val:
                return False
            head1 = head1.next
            head = head.next
        return True