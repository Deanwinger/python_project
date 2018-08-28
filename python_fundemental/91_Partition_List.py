# leetcode 86. 分隔链表
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        此版更復雜, 考虑了等于的情况, 
        三个临时链表, 86题只区分, 小于和大于等于两种情况
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return
        
        d1 = big =ListNode(0)
        d2 = equ =ListNode(0)
        d3 = sml =ListNode(0)
        p = head.next
        while head:
            if head.val > x:
                big.next = head
                big = big.next
                big.next = None
            elif head.val == x:
                equ.next = head
                equ = equ.next
                equ.next = None
            else:
                sml.next = head
                sml = sml.next
                sml.next = None
            head = p
            if not p:
                break
            p = p.next
        
        if d2.next:
            sml.next = d2.next
            if d1.next:
                equ.next = d1.next 
        else:
            if d1.next:
                sml.next = d1.next
        return d3.next
            

class Solution(object):
    def partition(self, head, x):
        """
        86题的解, 更简单
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return
        
        d1 = big =ListNode(0)
        d3 = sml =ListNode(0)
        p = head.next
        while head:
            if head.val >= x:
                big.next = head
                big = big.next
                big.next = None
            else:
                sml.next = head
                sml = sml.next
                sml.next = None
            head = p
            if not p:
                break
            p = p.next
            
        if d1.next:
            sml.next = d1.next
        return d3.next

# 8.28 重写, 非常elegant, 关键是head1.next = None, 杜绝了之前发生的错误
class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dum1 = head1 = ListNode(0)
        dum2 = head2 = ListNode(0)
        while head:
            if head.val < x:
                head1.next = head
                head = head.next
                head1 = head1.next
                head1.next = None
            else:
                head2.next = head
                head = head.next
                head2 = head2.next
                head2.next = None
        
        head1.next = dum2.next
        return dum1.next


if __name__ == "__main__":
    alist = [1,4,3,2,5,2,6]
    x = 3
    dummy = head = ListNode(0)
    while alist:
        head.next = ListNode(alist.pop(0))
        head = head.next
    s = Solution()
    d = s.partition(dummy.next, x)
    while d:
        print("partition result: ", d.val)
        d = d.next