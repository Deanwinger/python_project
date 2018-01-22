'''
反转链表
输入一个链表，反转链表后，输出链表的所有元素
'''

# 题16
# leetcode 206 和 92

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse_link_list(self, head):
        #同为206的解
        if not head:
            return 
        fast = head.next
        head.next = None
        while fast:
            slow = head
            head = fast
            fast = fast.next
            head.next = slow
            if fast is None:
                return head
        return head


if __name__=='__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    s = Solution()
    a = s.reverse_link_list(node1)
    n=15
    while n:
        print(a.val)
        a = a.next
        n -= 1
