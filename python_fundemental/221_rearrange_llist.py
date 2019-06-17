# leetcode 143. 重排链表


# 这题综合性很高, 可以反复多做几遍
# 思路: 先找到中点, 链表分为前后两段, 后半段逆转, 然后合并两个链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or head.next is None:
            return
        
        n = 0
        t = head
        while t:
            t = t.next
            n += 1
            
        # find the mid node
        left_start = pre = slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
         
        pre.next = None
        if n%2 == 0:
            # even
            mid = None
            right_start = slow
            r = self.reverse(right_start)
        else:
            # odd
            mid = slow
            right_start = slow.next
            mid.next = None
            r = self.reverse(right_start)
            print(r.val)
        self.merge(left_start, r, mid=mid)
        return
    
    def reverse(self, head):
        node = head.next
        head.next = None
        while node:
            tem = node.next
            node.next = head
            head = node
            node = tem
        return head

    # 这种代码说实在的, 辣眼睛        
    def merge(self, left, right, mid=None):
        s = t = ListNode(0)
        while left and right:
            left_tem = left.next
            right_tem = right.next
            t.next = left
            left.next = right
            t = t.next.next
            left = left_tem
            right = right_tem
        if mid:
            t.next = mid
        return s.next
        