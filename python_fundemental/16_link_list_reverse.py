'''
反转链表
输入一个链表，反转链表后，输出链表的所有元素
'''

# 题16
# leetcode 206 和 92
# 2019.2.13 redo

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # ac 通过 非常漂亮的原地修改
    def reverse_link_list(self, head):
        """
        1. 同为206的解        
        2. 解法1: 原地修改
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        p = head.next
        head.next = None
        while p:
            temp = p.next
            p.next = head
            head = p
            p = temp
        return head

    def reverse_link_list_v2(self, head):
        """
        1. 同为206的解        
        2. 解法2: 利用stack
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        if stack:
            dummy = head = stack.pop()
            while stack:
                head.next = stack.pop()
                head = head.next
            head.next = None
            return dummy
        else:
            return

    def reverse_link_list_v3(self, head):
        """
        1. 同为206的解        
        2. 解法2: 递归解法
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)



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
